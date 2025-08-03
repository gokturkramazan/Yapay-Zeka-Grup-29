const API_BASE_URL = 'http://localhost:8000/api'; // Saras backend runs on port 8000
const CURRENT_USER_ID = 'U1'; // This could be dynamic based on login

// Initialize jsPsych with Saras backend integration
const jsPsych = initJsPsych({
  on_finish: function () {
    const trials = jsPsych.data.get().values();

    // Filter out practice trials or non-test trials
    const testTrials = trials.filter(trial => 
      trial.trial_type === 'html-keyboard-response' && 
      trial.stimulus && 
      trial.response !== null
    );

    const responses = testTrials.map(t => t.response);
    const reaction_times = testTrials.map(t => t.rt);
    const correctResponses = testTrials.map(t => t.correct_response);

    // Calculate accuracy
    const accuracy = responses.filter((r, i) => r === correctResponses[i]).length / responses.length;
    const total_time = reaction_times.reduce((sum, rt) => sum + rt, 0);

    // Format data for Sara backend API
    const testResult = {
      user_id: CURRENT_USER_ID,
      test_type: "attention_stroop",
      responses: responses,
      reaction_times: reaction_times,
      accuracy: accuracy,
      total_time: total_time,
      timestamp: new Date().toISOString()
    };

    // Submit to Sara backend
    submitTestResult(testResult);
  }
});

// API Functions for Sara Backend

async function checkBackendHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    if (response.ok) {
      const data = await response.json();
      console.log('Backend Health:', data);
      return data.status === 'healthy';
    }
    return false;
  } catch (error) {
    console.error('Backend health check failed:', error);
    return false;
  }
}

async function submitTestResult(testResult) {
  try {
    const response = await fetch(`${API_BASE_URL}/test-result`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(testResult)
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    
    if (data.success) {
      alert("Test sonucu gönderildi! Dashboard güncelleniyor...");
      
      // Log Sara adaptive recommendation
      if (data.recommendation) {
        console.log('Adaptive Recommendation:', data.recommendation);
        console.log('Next Difficulty:', data.recommendation.next_difficulty);
        console.log('Performance Trend:', data.recommendation.performance_trend);
        console.log('Skill Level:', data.recommendation.skill_level);
        
        // Show badge notification if earned
        if (data.recommendation.suggested_achievement) {
          alert(`🎉 Yeni Rozet Kazandın: ${data.recommendation.suggested_achievement}!`);
        }
      }
      
      // Refresh the page to update dashboard
      location.reload();
    } else {
      throw new Error(data.message || 'Test sonucu gönderilemedi');
    }
  } catch (err) {
    console.error("Test sonucu gönderilirken hata:", err);
    alert("Test sonucu gönderilirken hata oluştu: " + err.message);
  }
}

async function fetchDashboardData(userId) {
  try {
    const response = await fetch(`${API_BASE_URL}/dashboard-data/${userId}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Dashboard verisi alınırken hata:', error);
    return null;
  }
}

async function fetchUserStats(userId) {
  try {
    const response = await fetch(`${API_BASE_URL}/user-stats/${userId}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('User stats alınırken hata:', error);
    return null;
  }
}

// Dashboard initialization and data loading
async function initializeDashboard() {
  // Check if backend is healthy
  const isHealthy = await checkBackendHealth();
  if (!isHealthy) {
    console.warn('Backend servisi erişilebilir değil. Fallback data kullanılıyor.');
    showFallbackDashboard();
    return;
  }

  // Fetch and display dashboard data
  const dashboardData = await fetchDashboardData(CURRENT_USER_ID);
  if (dashboardData) {
    updateDashboardUI(dashboardData);
    
    // Fetch additional user stats
    const userStats = await fetchUserStats(CURRENT_USER_ID);
    if (userStats) {
      console.log('User Statistics:', userStats);
      updateUserStatsUI(userStats);
    }
  } else {
    showFallbackDashboard();
  }
}

function updateDashboardUI(data) {
  // Update score and difficulty
  if (document.getElementById('skor-value')) {
    document.getElementById('skor-value').textContent = data.daily_score || '0';
  }
  if (document.getElementById('zorluk-value')) {
    document.getElementById('zorluk-value').textContent = data.next_difficulty || 'Bilinmiyor';
  }
  if (document.getElementById('rozet-count')) {
    document.getElementById('rozet-count').textContent = data.total_badges || '0';
  }

  // Update chart with Sara's data format
  if (data.score_history_for_chart && data.score_history_for_chart.length > 0) {
    updateChart(data.score_history_for_chart);
  }

  // Update badge notifications
  if (data.unlocked_badges && data.unlocked_badges.length > 0) {
    updateBadgeNotifications(data.unlocked_badges);
  }

  // Update badge collection
  updateBadgeCollection(data.all_badges || [], data.unlocked_badges || []);

  // Log additional Sara's backend data
  console.log('Performance Trend:', data.performance_trend);
  console.log('Skill Level:', data.skill_level);
  console.log('Cognitive Profile:', data.cognitive_profile);
  console.log('Behavior Type:', data.behavior_type);
}

function updateUserStatsUI(stats) {
  // You can add additional UI elements to display these stats
  console.log('Detailed User Stats:');
  console.log('- Skill Level:', stats.skill_level);
  console.log('- Cognitive Profile:', stats.cognitive_profile);
  console.log('- Behavior Type:', stats.behavior_type);
  console.log('- Average Reaction Time:', stats.reaction_time);
  console.log('- Average Accuracy:', stats.accuracy);
  console.log('- Memory Score:', stats.memory_score);
}

function updateChart(scoreHistory) {
  const chartElement = document.getElementById("chart");
  if (!chartElement) return;

  const labels = scoreHistory.map(entry => {
    const date = new Date(entry.date);
    return date.toLocaleDateString('tr-TR', { month: 'short', day: 'numeric' });
  });
  const scores = scoreHistory.map(entry => entry.score);

  // Destroy existing chart if it exists
  if (window.chartInstance) {
    window.chartInstance.destroy();
  }

  window.chartInstance = new Chart(chartElement, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: "Performans Skoru",
        data: scores,
        borderColor: "#667eea",
        backgroundColor: "rgba(102, 126, 234, 0.1)",
        borderWidth: 3,
        fill: true,
        tension: 0.4,
        pointBackgroundColor: "#667eea",
        pointBorderColor: "#ffffff",
        pointBorderWidth: 3,
        pointRadius: 6
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: "rgba(0,0,0,0.05)" }
        },
        x: {
          grid: { display: false }
        }
      }
    }
  });
}

function updateBadgeNotifications(unlockedBadges) {
  const notificationElement = document.getElementById("rozet-notification");
  if (!notificationElement) return;

  if (unlockedBadges && unlockedBadges.length > 0) {
    // Find the most recently awarded badge
    const sortedBadges = unlockedBadges.sort((a, b) => 
      new Date(b.awarded_at) - new Date(a.awarded_at)
    );
    const latestBadge = sortedBadges[0];
    
    notificationElement.innerHTML = `
      <h3>🎉 Yeni Rozet Kazandın!</h3>
      <p><strong>${latestBadge.badge_name}</strong> — ${latestBadge.badge_description}</p>
    `;
    notificationElement.style.display = 'block';
  }
}

function updateBadgeCollection(allBadges, unlockedBadges) {
  const badgeIcons = {
    "İstikrarlı Oyuncu": "🎯",
    "Keskin Göz": "👁️",
    "Puan Canavarı": "🦁", 
    "Dayanıklılık": "💪",
    "Dayanıklılık Savaşçısı": "⚔️",
    "Hız Şampiyonu": "⚡",
    "Mükemmeliyetçi": "💯"
  };

  const koleksiyon = document.getElementById("rozet-koleksiyonu");
  if (!koleksiyon) return;

  koleksiyon.innerHTML = "";

  // Create a map of unlocked badge IDs and names for quick lookup
  const unlockedBadgeIds = unlockedBadges.map(badge => badge.badge_id);
  const unlockedBadgeNames = unlockedBadges.map(badge => badge.badge_name);

  // If we have all badges data from Sara's backend
  if (allBadges && allBadges.length > 0) {
    allBadges.forEach(badge => {
      const isUnlocked = unlockedBadgeIds.includes(badge.badge_id);
      const div = document.createElement("div");
      div.className = `badge ${isUnlocked ? "aktif" : "kilitli"}`;
      div.innerHTML = `
        <span class="badge-icon">${isUnlocked ? (badgeIcons[badge.badge_name] || "🏅") : "🔒"}</span>
        <div class="badge-name">${badge.badge_name}</div>
      `;
      koleksiyon.appendChild(div);
    });
  } else {
    // Fallback: show unlocked badges + some common locked ones
    unlockedBadges.forEach(badge => {
      const div = document.createElement("div");
      div.className = "badge aktif";
      div.innerHTML = `
        <span class="badge-icon">${badgeIcons[badge.badge_name] || "🏅"}</span>
        <div class="badge-name">${badge.badge_name}</div>
      `;
      koleksiyon.appendChild(div);
    });

    // Add some common locked badges for visual completeness
    const commonBadges = ["Puan Canavarı", "Dayanıklılık Savaşçısı", "Mükemmeliyetçi"];
    commonBadges.forEach(badgeName => {
      if (!unlockedBadgeNames.includes(badgeName)) {
        const div = document.createElement("div");
        div.className = "badge kilitli";
        div.innerHTML = `
          <span class="badge-icon">🔒</span>
          <div class="badge-name">${badgeName}</div>
        `;
        koleksiyon.appendChild(div);
      }
    });
  }
}

function showFallbackDashboard() {
  // Show default values when backend is not available
  if (document.getElementById('skor-value')) {
    document.getElementById('skor-value').textContent = '0';
  }
  if (document.getElementById('zorluk-value')) {
    document.getElementById('zorluk-value').textContent = 'Kolay';
  }
  if (document.getElementById('rozet-count')) {
    document.getElementById('rozet-count').textContent = '0';
  }
  
  // Show empty chart
  updateChart([]);
  
  console.warn('Backend bağlantısı kurulamadı. Varsayılan veriler gösteriliyor.');
}

// Stroop test function with Sara's backend integration
function runTest() {
  if (!jsPsych) {
    alert('Test sistemi henüz hazır değil. Lütfen sayfayı yenileyin.');
    return;
  }

  const timeline = [
    {
      type: jsPsychHtmlKeyboardResponse,
      stimulus: '<div style="font-size: 48px; color: red; font-weight: bold; text-align: center; padding: 50px;">YEŞİL</div>',
      choices: ['k', 'y', 'm'],
      data: { correct_response: 'y' },
      prompt: '<p style="text-align: center; font-size: 18px;">Anlamına göre tuşa bas:<br><strong>K</strong>=Kırmızı, <strong>Y</strong>=Yeşil, <strong>M</strong>=Mavi</p>',
      trial_duration: 5000
    },
    {
      type: jsPsychHtmlKeyboardResponse,
      stimulus: '<div style="font-size: 48px; color: green; font-weight: bold; text-align: center; padding: 50px;">KIRMIZI</div>',
      choices: ['k', 'y', 'm'],
      data: { correct_response: 'k' },
      prompt: '<p style="text-align: center; font-size: 18px;">Anlamına göre tuşa bas:<br><strong>K</strong>=Kırmızı, <strong>Y</strong>=Yeşil, <strong>M</strong>=Mavi</p>',
      trial_duration: 5000
    },
    {
      type: jsPsychHtmlKeyboardResponse,
      stimulus: '<div style="font-size: 48px; color: blue; font-weight: bold; text-align: center; padding: 50px;">MAVİ</div>',
      choices: ['k', 'y', 'm'],
      data: { correct_response: 'm' },
      prompt: '<p style="text-align: center; font-size: 18px;">Anlamına göre tuşa bas:<br><strong>K</strong>=Kırmızı, <strong>Y</strong>=Yeşil, <strong>M</strong>=Mavi</p>',
      trial_duration: 5000
    }
  ];

  jsPsych.run(timeline);
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log('Initializing dashboard with Sara\'s backend...');
  initializeDashboard();
});

// Refresh data periodically (optional)
setInterval(() => {
  initializeDashboard();
}, 300000); // Refresh every 5 minutes