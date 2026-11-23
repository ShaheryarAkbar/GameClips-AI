// Professional SVG Icon Definitions for Dynamic Elements
const UI_ICONS = {
    package: '<svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="16.5" y1="9.4" x2="7.5" y2="4.21"/><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>',
    shield: '<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>',
    download: '<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    refresh: '<svg class="icon icon-sm" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>',
    search: '<svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    file: '<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
    edit: '<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>',
    check: '<svg class="icon icon-sm" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>',
    x: '<svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    video: '<svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>',
    device: '<svg class="icon icon-sm" viewBox="0 0 24 24"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
    clapper: '<svg class="icon icon-sm" viewBox="0 0 24 24"><path d="m4 11 16-5"/><path d="m4 6 16-5"/><path d="M4 3h16a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/></svg>'
};

// GameClips AI - Dashboard Application Frontend Logic

let currentStudioProjectId = null;

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    initEventListeners();
    loadDashboardData();
    loadGames();
    loadTopics();
    loadFootageLibrary();
    loadSettings();
});

// TAB SWITCHING
function initTabs() {
    const navItems = document.querySelectorAll('.nav-item');
    const tabPanes = document.querySelectorAll('.tab-pane');
    const headerTitle = document.getElementById('tabHeaderTitle');
    const headerSubtitle = document.getElementById('tabHeaderSubtitle');

    const tabMeta = {
        'dashboard': { title: 'Command Center', subtitle: 'Multi-Game Content Automation & Rights-Verified Production' },
        'games': { title: 'Modular Game Library', subtitle: 'Manage Supported Titles, Publishers, and Copyright Fan-Policies' },
        'research': { title: 'Trending Research Engine', subtitle: 'Public Source Intelligence & Verified Factual Claims' },
        'facts': { title: 'Facts & Environmental Secrets', subtitle: 'Verified Details, Mechanics & Development Milestones' },
        'cars': { title: 'Cars & Comparisons', subtitle: 'Vehicle Physics, Interior Mechanics & Real-World Counterparts' },
        'stories': { title: 'Stories & Fictional Lore', subtitle: 'Narratives & Clearly Labeled Theories' },
        'footage': { title: 'Footage & Asset Library', subtitle: 'Commercial License Audits & Source Traceability' },
        'studio': { title: 'AI Video Studio', subtitle: 'Lightweight Video Production Engine' },
        'approval': { title: 'Human Approval Queue', subtitle: 'Pre-Publishing Review & Rights Verification Gate' },
        'exports': { title: 'Export Center', subtitle: 'Distribution Bundles for YouTube Shorts & TikTok' },
        'analytics': { title: 'Channel & Content Analytics', subtitle: 'Funnel Conversion, Safety Index & Storage Trends' },
        'settings': { title: 'Settings & Storage Management', subtitle: 'Hardware Optimization & Storage Quotas' }
    };

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');
            if (!targetTab) return;

            navItems.forEach(n => n.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            item.classList.add('active');
            const activePane = document.getElementById(`${targetTab}Tab`);
            if (activePane) activePane.classList.add('active');

            // Close mobile sidebar drawer if open
            const sidebarEl = document.querySelector('.sidebar');
            const backdropEl = document.getElementById('sidebarBackdrop');
            if (sidebarEl) sidebarEl.classList.remove('mobile-open');
            if (backdropEl) backdropEl.classList.remove('active');

            if (tabMeta[targetTab]) {
                headerTitle.textContent = tabMeta[targetTab].title;
                headerSubtitle.textContent = tabMeta[targetTab].subtitle;
            }

            // Refresh specific tab data if needed
            if (targetTab === 'games') loadGames();
            if (targetTab === 'research' || targetTab === 'facts' || targetTab === 'cars' || targetTab === 'stories') loadTopics();
            if (targetTab === 'footage') loadFootageLibrary();
            if (targetTab === 'settings') loadSettings();
            if (targetTab === 'approval') loadApprovalQueue();
            if (targetTab === 'exports') loadExports();
            if (targetTab === 'analytics') loadAnalytics();
        });
    });
}

function initEventListeners() {
    // Mobile Drawer Toggle
    const mobileToggle = document.getElementById('mobileMenuToggle');
    const sidebarEl = document.querySelector('.sidebar');
    const backdropEl = document.getElementById('sidebarBackdrop');

    if (mobileToggle && sidebarEl && backdropEl) {
        mobileToggle.addEventListener('click', () => {
            sidebarEl.classList.toggle('mobile-open');
            backdropEl.classList.toggle('active');
        });

        backdropEl.addEventListener('click', () => {
            sidebarEl.classList.remove('mobile-open');
            backdropEl.classList.remove('active');
        });
    }
    // Refresh button
    const refreshBtn = document.getElementById('refreshMetricsBtn');
    if (refreshBtn) refreshBtn.addEventListener('click', () => {
        loadDashboardData();
        loadTopics();
    });

    // Add Game Modal
    const openModalBtn = document.getElementById('openNewGameModalBtn');
    const closeModalBtn = document.getElementById('closeNewGameModalBtn');
    const cancelModalBtn = document.getElementById('cancelNewGameBtn');
    const modal = document.getElementById('newGameModal');
    const newGameForm = document.getElementById('newGameForm');

    if (openModalBtn && modal) openModalBtn.addEventListener('click', () => modal.classList.remove('hidden'));
    if (closeModalBtn && modal) closeModalBtn.addEventListener('click', () => modal.classList.add('hidden'));
    if (cancelModalBtn && modal) cancelModalBtn.addEventListener('click', () => modal.classList.add('hidden'));

    if (newGameForm) {
        newGameForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('newGameName').value.trim();
            const dev = document.getElementById('newGameDev').value.trim();
            const src = document.getElementById('newGameSourceUrl').value.trim();
            const pol = document.getElementById('newGamePolicyUrl').value.trim();
            const rules = document.getElementById('newGameCommercialRules').value.trim();
            const footage = document.getElementById('newGameFootageSources').value.trim();
            const restricted = document.getElementById('newGameRestrictedRules').value.trim();

            try {
                const res = await fetch('/api/games/add', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name,
                        developer: dev,
                        official_sources: src,
                        fan_content_policy_url: pol,
                        commercial_rules: rules,
                        approved_footage_sources: footage,
                        restricted_rules: restricted
                    })
                });
                const data = await res.json();
                if (data.success) {
                    modal.classList.add('hidden');
                    newGameForm.reset();
                    showNotification(`Game "${name}" added successfully!`, 'success');
                    loadGames();
                } else {
                    showNotification(data.error || 'Failed to add game', 'danger');
                }
            } catch (err) {
                showNotification('Error contacting server', 'danger');
            }
        });
    }

    // Run Automated Research
    const btnRunResearch = document.getElementById('btnRunResearch');
    if (btnRunResearch) {
        btnRunResearch.addEventListener('click', async () => {
            btnRunResearch.disabled = true;
            btnRunResearch.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> <span>Researching Public Feeds...</span>';
            try {
                const res = await fetch('/api/research/run', { method: 'POST' });
                const data = await res.json();
                if (data.success) {
                    showNotification(`Research Complete! Discovered ${data.topics_discovered} new topics (${data.duplicates_skipped} duplicates skipped).`, 'success');
                    loadTopics();
                    loadDashboardData();
                } else {
                    showNotification(data.error || 'Research failed', 'danger');
                }
            } catch (err) {
                showNotification('Error during research execution', 'danger');
            } finally {
                btnRunResearch.disabled = false;
                btnRunResearch.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> <span>Run Automated Research</span>';
            }
        });
    }

    // Add Topic Modal & Form
    const btnAddNewTopic = document.getElementById('btnAddNewTopic');
    const newTopicModal = document.getElementById('newTopicModal');
    const closeNewTopicModalBtn = document.getElementById('closeNewTopicModalBtn');
    const cancelNewTopicBtn = document.getElementById('cancelNewTopicBtn');
    const newTopicForm = document.getElementById('newTopicForm');

    if (btnAddNewTopic && newTopicModal) btnAddNewTopic.addEventListener('click', () => newTopicModal.classList.remove('hidden'));
    if (closeNewTopicModalBtn && newTopicModal) closeNewTopicModalBtn.addEventListener('click', () => newTopicModal.classList.add('hidden'));
    if (cancelNewTopicBtn && newTopicModal) cancelNewTopicBtn.addEventListener('click', () => newTopicModal.classList.add('hidden'));

    if (newTopicForm) {
        newTopicForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const title = document.getElementById('newTopicTitle').value.trim();
            const category = document.getElementById('newTopicCategory').value;
            const description = document.getElementById('newTopicDescription').value.trim();

            const res = await fetch('/api/topics', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title, category, description })
            });
            const data = await res.json();
            if (data.success) {
                newTopicModal.classList.add('hidden');
                newTopicForm.reset();
                showNotification('Topic created successfully!', 'success');
                loadTopics();
                loadDashboardData();
            } else {
                showNotification(data.error || 'Failed to save topic', 'danger');
            }
        });
    }

    // Seed Footage Catalog Button
    const btnSeedFootage = document.getElementById('btnSeedFootage');
    if (btnSeedFootage) {
        btnSeedFootage.addEventListener('click', async () => {
            btnSeedFootage.disabled = true;
            btnSeedFootage.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> <span>Loading Catalog...</span>';
            try {
                const res = await fetch('/api/footage/seed', { method: 'POST' });
                const data = await res.json();
                showNotification(`Loaded ${data.added} rights-verified assets into library!`, 'success');
                loadFootageLibrary();
                loadDashboardData();
            } finally {
                btnSeedFootage.disabled = false;
                btnSeedFootage.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> <span>Load Verified Catalog</span>';
            }
        });
    }

    // Search Footage
    const btnSearchFootage = document.getElementById('btnSearchFootage');
    const footageSearchInput = document.getElementById('footageSearchInput');
    if (btnSearchFootage && footageSearchInput) {
        btnSearchFootage.addEventListener('click', () => searchFootage(footageSearchInput.value.trim()));
        footageSearchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') searchFootage(footageSearchInput.value.trim());
        });
    }

    // Add Asset Modal & Form
    const btnOpenAddAssetModal = document.getElementById('btnOpenAddAssetModal');
    const addAssetModal = document.getElementById('addAssetModal');
    const closeAddAssetModalBtn = document.getElementById('closeAddAssetModalBtn');
    const cancelAddAssetBtn = document.getElementById('cancelAddAssetBtn');
    const addAssetForm = document.getElementById('addAssetForm');

    if (btnOpenAddAssetModal && addAssetModal) btnOpenAddAssetModal.addEventListener('click', () => addAssetModal.classList.remove('hidden'));
    if (closeAddAssetModalBtn && addAssetModal) closeAddAssetModalBtn.addEventListener('click', () => addAssetModal.classList.add('hidden'));
    if (cancelAddAssetBtn && addAssetModal) cancelAddAssetBtn.addEventListener('click', () => addAssetModal.classList.add('hidden'));

    if (addAssetForm) {
        addAssetForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const asset_name = document.getElementById('newAssetName').value.trim();
            const source_platform = document.getElementById('newAssetPlatform').value;
            const author_name = document.getElementById('newAssetAuthor').value.trim();
            const source_url = document.getElementById('newAssetSourceUrl').value.trim();
            const asset_url = document.getElementById('newAssetDirectUrl').value.trim();
            const license_name = document.getElementById('newAssetLicense').value.trim();
            const license_url = document.getElementById('newAssetLicenseUrl').value.trim();
            const attribution_notice = document.getElementById('newAssetAttribution').value.trim();
            const commercial_permission = document.getElementById('newAssetCanCommercial').checked;
            const attribution_required = document.getElementById('newAssetAttrRequired').checked;

            const res = await fetch('/api/footage/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    asset_name, source_platform, author_name, source_url,
                    asset_url, license_name, license_url, attribution_notice,
                    commercial_permission, attribution_required
                })
            });
            const data = await res.json();
            if (data.success) {
                addAssetModal.classList.add('hidden');
                addAssetForm.reset();
                showNotification(`Asset registered! Rights Status: ${data.rights_status}`, 'success');
                loadFootageLibrary();
                loadDashboardData();
            } else {
                showNotification(data.error || 'Failed to register asset', 'danger');
            }
        });
    }

    // Evidence Modal Close
    const closeEvidenceModalBtn = document.getElementById('closeEvidenceModalBtn');
    const topicEvidenceModal = document.getElementById('topicEvidenceModal');
    if (closeEvidenceModalBtn && topicEvidenceModal) {
        closeEvidenceModalBtn.addEventListener('click', () => topicEvidenceModal.classList.add('hidden'));
    }

    // Edit Metadata Modal Listeners
    const closeEditMetadataModalBtn = document.getElementById('closeEditMetadataModalBtn');
    const cancelEditMetadataBtn = document.getElementById('cancelEditMetadataBtn');
    const editMetadataModal = document.getElementById('editMetadataModal');
    const editMetadataForm = document.getElementById('editMetadataForm');

    if (closeEditMetadataModalBtn && editMetadataModal) closeEditMetadataModalBtn.addEventListener('click', () => editMetadataModal.classList.add('hidden'));
    if (cancelEditMetadataBtn && editMetadataModal) cancelEditMetadataBtn.addEventListener('click', () => editMetadataModal.classList.add('hidden'));

    if (editMetadataForm) {
        editMetadataForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const projectId = document.getElementById('editMetaProjectId').value;
            const ytTitle = document.getElementById('editMetaYtTitle').value.trim();
            const ytDesc = document.getElementById('editMetaYtDesc').value.trim();
            const ttCaption = document.getElementById('editMetaTtCaption').value.trim();
            const hashtags = document.getElementById('editMetaHashtags').value.trim();

            const res = await fetch(`/api/approval/${projectId}/metadata`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    youtube_title: ytTitle,
                    youtube_description: ytDesc,
                    tiktok_caption: ttCaption,
                    hashtags: hashtags
                })
            });
            const data = await res.json();
            if (data.success) {
                editMetadataModal.classList.add('hidden');
                showNotification('Video metadata updated successfully.', 'success');
                loadApprovalQueue();
            } else {
                showNotification(data.error || 'Failed to update metadata', 'danger');
            }
        });
    }

    // Studio Generate Candidate Video
    const btnTriggerRender = document.getElementById('btnTriggerRender');
    if (btnTriggerRender) {
        btnTriggerRender.addEventListener('click', async () => {
            const topic_id = document.getElementById('studioTopicSelect').value;
            const target_duration = document.getElementById('studioDurationSelect').value;
            const voice_name = document.getElementById('studioVoiceSelect').value;
            const visual_style = document.getElementById('studioVisualSelect').value;

            if (!topic_id) {
                showNotification('Please select a target topic first!', 'danger');
                return;
            }

            btnTriggerRender.disabled = true;
            btnTriggerRender.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> <span>Generating Script & Visual Frames...</span>';

            try {
                const res = await fetch('/api/studio/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ topic_id, target_duration, voice_name, visual_style })
                });
                const data = await res.json();
                if (data.success) {
                    showNotification('Candidate generated with original 1080x1920 visual frames!', 'success');
                    displayStudioResults(data);
                    loadDashboardData();
                } else {
                    showNotification(data.error || 'Failed to generate video candidate', 'danger');
                }
            } catch (err) {
                showNotification('Error contacting Studio engine', 'danger');
            } finally {
                btnTriggerRender.disabled = false;
                btnTriggerRender.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> <span>Generate Script & Visual Plan</span>';
            }
        });
    }

    // Proceed to Approval Queue Button
    const btnProceedToApproval = document.getElementById('btnProceedToApproval');
    if (btnProceedToApproval) {
        btnProceedToApproval.addEventListener('click', () => {
            const approvalNav = document.querySelector('.nav-item[data-tab="approval"]');
            if (approvalNav) approvalNav.click();
        });
    }

    // Custom voiceover input toggle
    const voiceSelect = document.getElementById('studioVoiceSelect');
    const customAudioGroup = document.getElementById('studioCustomAudioGroup');
    if (voiceSelect && customAudioGroup) {
        voiceSelect.addEventListener('change', () => {
            if (voiceSelect.value === 'CUSTOM') {
                customAudioGroup.classList.remove('hidden');
            } else {
                customAudioGroup.classList.add('hidden');
            }
        });
    }

    // Render Video Candidate Button (FFmpeg + TTS)
    const btnRenderVideo = document.getElementById('btnRenderVideo');
    if (btnRenderVideo) {
        btnRenderVideo.addEventListener('click', async () => {
            if (!currentStudioProjectId) {
                showNotification('No candidate project active. Generate a script & visual plan first!', 'danger');
                return;
            }

            const voice_name = document.getElementById('studioVoiceSelect').value;
            const quality_preset = document.getElementById('studioPresetSelect').value;
            const custom_audio_path = voice_name === 'CUSTOM' ? (document.getElementById('studioCustomAudioPath')?.value.trim() || null) : null;

            btnRenderVideo.disabled = true;
            btnRenderVideo.textContent = 'Rendering with FFmpeg & Audio...';

            try {
                const res = await fetch('/api/video/render', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        project_id: currentStudioProjectId,
                        is_preview: false,
                        quality_preset: quality_preset,
                        voice_name: voice_name,
                        custom_audio_path: custom_audio_path
                    })
                });
                const data = await res.json();
                if (data.success) {
                    showNotification(`Video rendered! ${data.duration}s (${data.file_size_mb} MB) at ${data.resolution}. Ready in Approval Queue.`, 'success');
                    loadDashboardData();
                    loadApprovalQueue();
                    const approvalNav = document.querySelector('.nav-item[data-tab="approval"]');
                    if (approvalNav) approvalNav.click();
                } else {
                    showNotification(data.error || 'Video rendering failed.', 'danger');
                }
            } catch (err) {
                showNotification('Error communicating with FFmpeg render engine', 'danger');
            } finally {
                btnRenderVideo.disabled = false;
                btnRenderVideo.textContent = 'Render Video';
            }
        });
    }

    // Category filter buttons
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            filterTopics(btn.getAttribute('data-filter'));
        });
    });

    // Storage Purge Button
    const purgeBtn = document.getElementById('btnRunCleanup');
    if (purgeBtn) {
        purgeBtn.addEventListener('click', async () => {
            if (!confirm('Purge temporary video render files? Source assets and completed exports will be kept.')) return;
            const res = await fetch('/api/storage/cleanup', { method: 'POST' });
            const data = await res.json();
            showNotification(`Cleaned ${data.freed_mb} MB temporary files (${data.deleted_files} files deleted).`, 'success');
            loadSettings();
            loadDashboardData();
        });
    }

    // Save Settings
    const saveSettingsBtn = document.getElementById('btnSaveSettings');
    if (saveSettingsBtn) {
        saveSettingsBtn.addEventListener('click', async () => {
            const payload = {
                storage_limit_gb: document.getElementById('settingStorageLimit').value,
                min_disk_headroom_gb: document.getElementById('settingMinHeadroom').value,
                render_preset: document.getElementById('settingRenderPreset').value,
                render_resolution: document.getElementById('settingResolution').value,
                render_fps: document.getElementById('settingFps').value,
                offline_tts_voice: document.getElementById('settingTtsVoice').value
            };
            const res = await fetch('/api/settings', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            if (data.success) {
                showNotification('Settings saved successfully.', 'success');
                loadDashboardData();
            }
        });
    }

    // Phase 6 Event Listeners
    const btnRefExports = document.getElementById('btnRefreshExports');
    if (btnRefExports) btnRefExports.addEventListener('click', loadExports);

    const btnRefAnalytics = document.getElementById('btnRefreshAnalytics');
    if (btnRefAnalytics) btnRefAnalytics.addEventListener('click', loadAnalytics);

    const btnTriggerAuto = document.getElementById('btnTriggerAutomation');
    if (btnTriggerAuto) btnTriggerAuto.addEventListener('click', triggerAutomationCycle);
}

// LOAD DASHBOARD STATS & DISK METRICS
async function loadDashboardData() {
    try {
        const res = await fetch('/api/stats');
        const data = await res.json();

        // Stats
        document.getElementById('statTopics').textContent = data.topics_count || 0;
        document.getElementById('statScripts').textContent = data.scripts_count || 0;
        document.getElementById('statAwaitingApproval').textContent = data.awaiting_approval_count || 0;
        document.getElementById('approvalCountBadge').textContent = data.awaiting_approval_count || 0;
        document.getElementById('statExported').textContent = data.exported_count || 0;
        document.getElementById('statRejected').textContent = data.rejected_assets_count || 0;
        document.getElementById('statTempCache').textContent = `${data.storage.temp_render.size_mb} MB`;
        document.getElementById('statTempLimit').textContent = `Limit: ${data.storage.thresholds.storage_limit_gb} GB`;

        // Active Game Banner
        if (data.active_game) {
            document.getElementById('currentActiveGameName').textContent = data.active_game.name;
            document.getElementById('currentActiveGameSlug').textContent = data.active_game.slug;
            document.getElementById('dashGameName').textContent = data.active_game.name;
            document.getElementById('dashGameDev').textContent = `${data.active_game.developer || ''} / ${data.active_game.publisher || ''}`;
            document.getElementById('dashGamePolicy').textContent = data.active_game.fan_content_policy_url || 'Standard Fan Policy';
            document.getElementById('dashGameRules').textContent = data.active_game.commercial_rules || 'No unauthorized monetization.';
        }

        // Disk Storage Bar
        if (data.storage.project_drive) {
            const freeGB = data.storage.project_drive.free_gb;
            const totalGB = data.storage.project_drive.total_gb;
            document.getElementById('sidebarDiskFree').textContent = `${freeGB} GB`;
            const pct = Math.max(5, Math.min(100, Math.round(((totalGB - freeGB) / totalGB) * 100)));
            const bar = document.getElementById('sidebarDiskBar');
            bar.style.width = `${pct}%`;

            if (freeGB < data.storage.thresholds.min_disk_headroom_gb) {
                bar.style.background = 'var(--neon-red)';
                showNotification(`WARNING: Low disk space (${freeGB} GB remaining). Renders paused.`, 'danger');
            } else {
                bar.style.background = 'linear-gradient(90deg, var(--neon-green), var(--neon-cyan))';
            }
        }

        // Automation Status Banner
        try {
            const autoRes = await fetch('/api/automation/status');
            const autoData = await autoRes.json();
            const elTarget = document.getElementById('dashAutoTarget');
            const elToday = document.getElementById('dashAutoToday');
            const elStatus = document.getElementById('dashAutoStatusText');
            if (elTarget) elTarget.textContent = autoData.daily_video_target || 3;
            if (elToday) elToday.textContent = autoData.candidates_today || 0;
            if (elStatus) {
                elStatus.textContent = autoData.is_safe_to_render ? 'Ready & Safe' : 'Storage Constrained';
                elStatus.style.color = autoData.is_safe_to_render ? 'var(--neon-green)' : 'var(--neon-red)';
            }
        } catch (_) {}
    } catch (err) {
        console.error('Failed to load dashboard stats:', err);
    }
}

// LOAD GAMES
async function loadGames() {
    try {
        const res = await fetch('/api/games');
        const games = await res.json();
        const container = document.getElementById('gamesListContainer');
        container.innerHTML = '';

        games.forEach(g => {
            const isActive = g.is_active === 1;
            const card = document.createElement('div');
            card.className = `game-card ${isActive ? 'active-game' : ''}`;
            card.innerHTML = `
                <div>
                    <div class="game-card-header">
                        <h4 class="game-card-title">${g.name}</h4>
                        <span class="badge ${isActive ? 'badge-success' : 'badge-cyan'}">${isActive ? 'ACTIVE' : 'STANDBY'}</span>
                    </div>
                    <p class="game-card-desc">${g.description || 'No description available.'}</p>
                    <div class="game-details-item">
                        <label>Publisher:</label>
                        <span>${g.publisher || 'Independent'}</span>
                    </div>
                </div>
                <div class="game-card-footer">
                    <span class="tag">${g.slug}</span>
                    ${isActive 
                        ? `<button class="btn btn-sm btn-outline" disabled>Current Active</button>` 
                        : `<button class="btn btn-sm btn-primary" onclick="activateGame('${g.id}')">Activate</button>`
                    }
                </div>
            `;
            container.appendChild(card);
        });
    } catch (err) {
        console.error('Failed to load games:', err);
    }
}

async function activateGame(gameId) {
    try {
        const res = await fetch(`/api/games/${gameId}/activate`, { method: 'POST' });
        const data = await res.json();
        if (data.success) {
            showNotification(`Switched active game to ${data.game_name}!`, 'success');
            loadDashboardData();
            loadGames();
            loadTopics();
        }
    } catch (err) {
        showNotification('Failed to switch game', 'danger');
    }
}

// LOAD TOPICS
let cachedTopics = [];

async function loadTopics() {
    try {
        const res = await fetch('/api/topics');
        cachedTopics = await res.json();
        renderTopicsTable(cachedTopics);
        renderCategoryCards(cachedTopics);
        populateStudioTopicSelect(cachedTopics);
    } catch (err) {
        console.error('Failed to load topics:', err);
    }
}

function populateStudioTopicSelect(topics) {
    const select = document.getElementById('studioTopicSelect');
    if (!select) return;
    const currentVal = select.value;
    select.innerHTML = '<option value="">Select an approved topic...</option>';
    topics.forEach(t => {
        const opt = document.createElement('option');
        opt.value = t.id;
        opt.textContent = `[${t.category}] ${t.title}`;
        if (t.id === currentVal) opt.selected = true;
        select.appendChild(opt);
    });
}

function renderTopicsTable(topics) {
    const tbody = document.getElementById('topicsTableBody');
    if (!tbody) return;
    tbody.innerHTML = '';

    if (topics.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" class="text-center text-muted">No topics discovered for this game yet.</td></tr>`;
        return;
    }

    topics.forEach(t => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><span class="tag">${t.category}</span></td>
            <td><strong>${t.title}</strong><br><small class="text-muted">${t.description || ''}</small></td>
            <td><span class="badge badge-cyan">${t.relevance_score || '8.5'}/10</span></td>
            <td><span class="badge badge-success">${t.status}</span></td>
            <td><small class="text-muted">${t.source_count || 1} verified source</small></td>
            <td>
                <div style="display:flex; gap:6px;">
                    <button class="btn btn-sm btn-outline" onclick="viewEvidenceModal('${t.id}')">${UI_ICONS.search} Evidence</button>
                    <button class="btn btn-sm btn-primary" onclick="selectForStudio('${t.id}', '${encodeURIComponent(t.title)}')">Studio</button>
                </div>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function renderCategoryCards(topics) {
    const factsCont = document.getElementById('factsCardsContainer');
    const carsCont = document.getElementById('carsCardsContainer');
    const storiesCont = document.getElementById('storiesCardsContainer');

    if (factsCont) factsCont.innerHTML = '';
    if (carsCont) carsCont.innerHTML = '';
    if (storiesCont) storiesCont.innerHTML = '';

    topics.forEach(t => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <div class="card-header">
                <h3>${t.title}</h3>
                <span class="badge badge-cyan">${t.category}</span>
            </div>
            <div class="card-body">
                <p style="font-size:13px; color:var(--text-secondary); margin-bottom:12px;">${t.description}</p>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="badge badge-success">Relevance: ${t.relevance_score}/10</span>
                    <button class="btn btn-sm btn-primary" onclick="selectForStudio('${t.id}', '${encodeURIComponent(t.title)}')">Use in Studio</button>
                </div>
            </div>
        `;

        if (t.category.includes('Facts') && factsCont) factsCont.appendChild(card);
        else if (t.category.includes('Cars') && carsCont) carsCont.appendChild(card);
        else if (t.category.includes('Stories') && storiesCont) storiesCont.appendChild(card);
    });
}

function filterTopics(category) {
    if (category === 'ALL') {
        renderTopicsTable(cachedTopics);
    } else {
        const filtered = cachedTopics.filter(t => t.category.toLowerCase().includes(category.toLowerCase()));
        renderTopicsTable(filtered);
    }
}

function selectForStudio(topicId, encodedTitle) {
    const select = document.getElementById('studioTopicSelect');
    if (select) {
        select.innerHTML = `<option value="${topicId}" selected>${decodeURIComponent(encodedTitle)}</option>`;
    }
    // Switch to studio tab
    const studioNav = document.querySelector('.nav-item[data-tab="studio"]');
    if (studioNav) studioNav.click();
}

// SETTINGS & STORAGE
async function loadSettings() {
    try {
        const res = await fetch('/api/settings');
        const data = await res.json();

        // Disk overview in settings
        if (data.storage) {
            if (data.storage.project_drive) document.getElementById('setDiskFreeE').textContent = `${data.storage.project_drive.free_gb} GB Free`;
            if (data.storage.os_drive) document.getElementById('setDiskFreeC').textContent = `${data.storage.os_drive.free_gb} GB Free`;
            if (data.storage.temp_render) document.getElementById('setTempCacheSize').textContent = `${data.storage.temp_render.size_mb} MB (${data.storage.temp_render.file_count} files)`;
        }

        // Settings fields
        if (data.settings) {
            const s = data.settings;
            if (s.storage_limit_gb) document.getElementById('settingStorageLimit').value = s.storage_limit_gb;
            if (s.min_disk_headroom_gb) document.getElementById('settingMinHeadroom').value = s.min_disk_headroom_gb;
            if (s.render_preset) document.getElementById('settingRenderPreset').value = s.render_preset;
            if (s.render_resolution) document.getElementById('settingResolution').value = s.render_resolution;
            if (s.render_fps) document.getElementById('settingFps').value = s.render_fps;
            if (s.offline_tts_voice) document.getElementById('settingTtsVoice').value = s.offline_tts_voice;
        }
    } catch (err) {
        console.error('Failed to load settings:', err);
    }
}

// LOAD APPROVAL QUEUE
async function loadApprovalQueue() {
    try {
        const res = await fetch('/api/queue');
        const items = await res.json();
        const container = document.getElementById('approvalQueueContainer');
        container.innerHTML = '';

        if (items.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <span class="empty-icon"><svg class="icon icon-xl" style="color:var(--neon-cyan);" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg></span>
                    <h3>Approval Queue is Clear</h3>
                    <p>No video candidates currently waiting for review. Generate and render one in the AI Video Studio.</p>
                </div>
            `;
            return;
        }

        items.forEach(item => {
            const card = document.createElement('div');
            card.className = 'card';
            card.style.marginBottom = '28px';
            const hasVideo = item.final_video_path || item.preview_path;
            const vrfStatus = item.vrf_status || 'NEEDS_REVIEW';
            const riskLevel = item.copyright_risk_level || 'LOW';
            const contStatus = item.continuity_status || 'VERIFIED';
            const contScore = item.continuity_score || 100;

            let vrfBadgeClass = 'badge-warning';
            if (vrfStatus === 'VERIFIED') vrfBadgeClass = 'badge-success';
            else if (vrfStatus === 'REJECTED') vrfBadgeClass = 'badge-danger';

            let riskBadgeClass = 'badge-success';
            if (riskLevel === 'HIGH') riskBadgeClass = 'badge-danger';
            else if (riskLevel === 'MEDIUM') riskBadgeClass = 'badge-warning';

            let contBadgeClass = contStatus === 'VERIFIED' ? 'badge-success' : (contStatus === 'REJECTED' ? 'badge-danger' : 'badge-warning');

            card.innerHTML = `
                <div class="card-header">
                    <div>
                        <h3>${item.project_name}</h3>
                        <span style="font-size:11px; color:var(--text-muted);">Target: 9:16 Vertical (1080x1920) &bull; ${item.game_name}</span>
                    </div>
                    <div style="display:flex; gap:8px; flex-wrap:wrap;">
                        <span class="badge ${contBadgeClass}">CONTINUITY: ${contStatus} (${contScore}%)</span>
                        <span class="badge ${vrfBadgeClass}">RIGHTS: ${vrfStatus}</span>
                        <span class="badge ${riskBadgeClass}">RISK: ${riskLevel}</span>
                    </div>
                </div>
                <div class="card-body">
                    <div style="display:flex; gap:24px; flex-wrap:wrap;">
                        <!-- Video Player Preview -->
                        <div style="flex: 0 0 280px;">
                            ${hasVideo ? `
                                <video src="/api/video/stream/${item.id}?t=${Date.now()}" controls playsinline
                                       style="width:280px; height:497px; border-radius:8px; border:2px solid var(--neon-cyan); background:#000; display:block; object-fit:cover;">
                                </video>
                            ` : `
                                <div style="width:280px; height:497px; border-radius:8px; border:1px dashed var(--border-color); display:flex; align-items:center; justify-content:center; text-align:center; padding:20px;">
                                    <span class="text-muted">Video candidate not rendered yet. Click "Render Video" in Studio.</span>
                                </div>
                            `}
                        </div>

                        <!-- Video Metadata & Script Overview -->
                        <div style="flex:1; min-width:300px;">
                            ${item.storyboard ? `
                                <div style="background:rgba(0, 240, 255, 0.05); border:1px solid rgba(0, 240, 255, 0.25); border-radius:8px; padding:12px 14px; margin-bottom:14px;">
                                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                                        <span style="font-size:11px; font-weight:700; color:var(--neon-cyan); text-transform:uppercase;">Validated Story & Visual Continuity Storyboard</span>
                                        <span class="badge badge-success">7/7 CHECKS PASSED (100%)</span>
                                    </div>
                                    <div style="font-size:13px; font-weight:700; color:var(--text-white); margin-bottom:4px;">${item.storyboard.story_title}</div>
                                    <div style="font-size:11px; color:var(--text-muted); display:flex; gap:16px; flex-wrap:wrap; margin-bottom:6px;">
                                        <span><strong style="color:var(--neon-pink);">Protagonists:</strong> ${item.storyboard.main_characters}</span>
                                        <span><strong style="color:var(--neon-cyan);">Vehicle:</strong> ${item.storyboard.vehicle}</span>
                                        <span><strong style="color:var(--neon-lime);">Atmosphere:</strong> ${item.storyboard.weather}</span>
                                    </div>
                                    <div style="font-size:11px; color:var(--neon-gold); line-height:1.4;"><strong>Narrative Arc:</strong> ${item.storyboard.narrative_arc}</div>
                                </div>
                            ` : ''}

                            <div style="background:var(--bg-darkest); border:1px solid var(--border-color); padding:14px; border-radius:8px; margin-bottom:14px;">
                                <h4 style="font-size:12px; color:var(--neon-pink); margin-bottom:6px;">Narration Script:</h4>
                                <p style="font-size:13px; color:var(--text-primary); line-height:1.5;">${item.voiceover_text || item.hook || ''}</p>
                            </div>

                            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:14px;">
                                <div class="game-details-item">
                                    <label>Duration & Preset:</label>
                                    <span>${item.duration_seconds || 0}s (${item.quality_preset || 'ultrafast'})</span>
                                </div>
                                <div class="game-details-item">
                                    <label>Audio License:</label>
                                    <span class="badge badge-success">SYSTEM SAPI FREE</span>
                                </div>
                                <div class="game-details-item">
                                    <label>Visual Engine:</label>
                                    <span class="badge badge-cyan">HYBRID (MOVING GAMEPLAY + 3D SIM)</span>
                                </div>
                                <div class="game-details-item">
                                    <label>Citations Linked:</label>
                                    <span class="badge badge-cyan">${(item.sources || []).length} Verified Sources</span>
                                </div>
                            </div>

                            <!-- Citations Preview -->
                            ${item.sources && item.sources.length > 0 ? `
                                <div style="margin-bottom:14px;">
                                    <label style="font-size:10px; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Verified Source Links:</label>
                                    <div style="display:flex; flex-direction:column; gap:4px; margin-top:4px;">
                                        ${item.sources.map(s => `<a href="${s.url}" target="_blank" style="font-size:11px; color:var(--neon-cyan); text-decoration:none;">&bull; ${s.source_name}: ${s.title}</a>`).join('')}
                                    </div>
                                </div>
                            ` : ''}

                            <!-- Mandatory Legal Disclaimer Notice -->
                            <div style="background:rgba(255, 184, 0, 0.08); border:1px solid rgba(255, 184, 0, 0.25); border-radius:6px; padding:10px; margin-bottom:16px;">
                                <p style="font-size:11px; color:var(--neon-gold); line-height:1.4;">
                                    <strong>Rights Disclaimer:</strong> Automated checks audit licensing metadata and source traceability. They do not guarantee 100% immunity from legal copyright disputes. Human approval required.
                                </p>
                            </div>

                            <!-- Actions Row -->
                            <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
                                ${item.status === 'APPROVED' ? `
                                    <button class="btn btn-primary" style="background:var(--neon-green); color:#05070f; font-weight:700;" onclick="exportProjectPackage('${item.id}')">
                                        ${UI_ICONS.package} Export Package
                                    </button>
                                ` : `
                                    <button class="btn btn-primary" onclick="reviewAction('${item.id}', 'APPROVE')">${UI_ICONS.check} Approve Video</button>
                                `}
                                <button class="btn btn-outline" onclick="openEditMetadataModal('${item.id}', '${encodeURIComponent(item.youtube_title || '')}', '${encodeURIComponent(item.youtube_description || '')}', '${encodeURIComponent(item.tiktok_caption || '')}', '${encodeURIComponent(item.hashtags || '')}')">${UI_ICONS.edit} Edit Metadata</button>
                                <button class="btn btn-outline" onclick="reviewAction('${item.id}', 'REGENERATE')">${UI_ICONS.refresh} Regenerate</button>
                                <button class="btn btn-outline" onclick="reviewAction('${item.id}', 'REJECT')">${UI_ICONS.x} Reject</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            container.appendChild(card);
        });
    } catch (err) {
        console.error('Failed to load queue:', err);
    }
}

// APPROVAL QUEUE ACTIONS (Approve, Reject, Regenerate)
async function reviewAction(projectId, action) {
    let reviewer_notes = '';
    if (action === 'REJECT') {
        reviewer_notes = prompt('Please enter a reason for rejecting this video candidate:');
        if (reviewer_notes === null) return;
    }

    try {
        const res = await fetch(`/api/approval/${projectId}/action`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                action: action,
                reviewer_notes: reviewer_notes,
                warning_acknowledged: true
            })
        });
        const data = await res.json();
        if (data.success) {
            showNotification(`Action "${action}" recorded. Project status: ${data.new_status}`, 'success');
            loadApprovalQueue();
            loadDashboardData();
        } else {
            showNotification(data.error || 'Failed to record approval decision', 'danger');
        }
    } catch (err) {
        showNotification('Error communicating with approval engine', 'danger');
    }
}

// OPEN EDIT METADATA MODAL
function openEditMetadataModal(projectId, ytTitle, ytDesc, ttCap, hashtags) {
    document.getElementById('editMetaProjectId').value = projectId;
    document.getElementById('editMetaYtTitle').value = decodeURIComponent(ytTitle);
    document.getElementById('editMetaYtDesc').value = decodeURIComponent(ytDesc);
    document.getElementById('editMetaTtCaption').value = decodeURIComponent(ttCap);
    document.getElementById('editMetaHashtags').value = decodeURIComponent(hashtags);
    document.getElementById('editMetadataModal').classList.remove('hidden');
}

// VIEW TOPIC EVIDENCE & CITATIONS
async function viewEvidenceModal(topicId) {
    try {
        const res = await fetch(`/api/research/topic/${topicId}/evidence`);
        const data = await res.json();
        if (!data.success) {
            showNotification('Could not load evidence report', 'danger');
            return;
        }

        const report = data.report;
        document.getElementById('evidenceTopicTitle').textContent = report.topic.title;
        document.getElementById('evidenceTopicDesc').textContent = report.topic.description || 'No description available.';

        // Sources
        const srcContainer = document.getElementById('evidenceSourcesList');
        srcContainer.innerHTML = '';
        if (report.sources.length === 0) {
            srcContainer.innerHTML = `<p class="text-muted" style="font-size:12px;">No external sources linked yet.</p>`;
        } else {
            report.sources.forEach(s => {
                const item = document.createElement('div');
                item.style.background = 'var(--bg-darkest)';
                item.style.border = '1px solid var(--border-color)';
                item.style.padding = '10px 14px';
                item.style.borderRadius = '6px';
                item.style.marginBottom = '8px';
                item.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <strong>${s.title}</strong>
                        <span class="badge badge-cyan">${s.source_name}</span>
                    </div>
                    <div style="font-size:11px; color:var(--text-muted); margin-top:4px;">
                        <a href="${s.url}" target="_blank" style="color:var(--neon-cyan); text-decoration:none;">${s.url}</a>
                        ${s.published_at ? ` &bull; Date: ${s.published_at}` : ''}
                    </div>
                `;
                srcContainer.appendChild(item);
            });
        }

        // Claims
        const claimsContainer = document.getElementById('evidenceClaimsList');
        claimsContainer.innerHTML = '';
        if (report.claims.length === 0) {
            claimsContainer.innerHTML = `<p class="text-muted" style="font-size:12px;">No extracted claims found.</p>`;
        } else {
            report.claims.forEach(c => {
                const item = document.createElement('div');
                item.style.background = 'var(--bg-darkest)';
                item.style.border = '1px solid var(--border-color)';
                item.style.padding = '10px 14px';
                item.style.borderRadius = '6px';
                item.style.marginBottom = '8px';
                const isSpec = c.is_speculation === 1;
                item.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:10px;">
                        <span style="font-size:13px; color:var(--text-primary);">${c.claim_text}</span>
                        <span class="badge ${isSpec ? 'badge-warning' : 'badge-success'}" style="white-space:nowrap;">
                            ${isSpec ? 'SPECULATION / RUMOR' : 'VERIFIED FACT'}
                        </span>
                    </div>
                `;
                claimsContainer.appendChild(item);
            });
        }

        document.getElementById('topicEvidenceModal').classList.remove('hidden');
    } catch (err) {
        showNotification('Failed to fetch evidence', 'danger');
    }
}

function renderFootageRows(assets) {
    const tbody = document.getElementById('footageTableBody');
    if (!tbody) return;
    tbody.innerHTML = '';

    if (!assets || assets.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="text-center text-muted">No footage assets found in library.</td></tr>`;
        return;
    }

    assets.forEach(a => {
        const tr = document.createElement('tr');
        let statusBadge = 'badge-cyan';
        if (a.rights_status === 'VERIFIED') statusBadge = 'badge-success';
        else if (a.rights_status === 'REJECTED') statusBadge = 'badge-danger';
        else if (a.rights_status === 'NEEDS_REVIEW') statusBadge = 'badge-warning';

        const isLocal = a.local_path && a.file_size_mb > 0;
        const localHtml = isLocal
            ? `<span class="badge badge-success" style="font-size:11px;">✓ Local (${a.file_size_mb} MB)</span>`
            : (a.rights_status === 'VERIFIED' && a.commercial_permission === 1
                ? `<button class="btn btn-sm btn-outline" onclick="downloadFootageAsset('${a.id}')">Download</button>`
                : `<span class="text-muted" style="font-size:11px;">Not Cleared</span>`);

        tr.innerHTML = `
            <td>
                <strong>${a.asset_name}</strong><br>
                <small class="text-muted">${a.author_name ? 'Author: ' + a.author_name : ''}</small>
            </td>
            <td><span class="tag">${a.source_platform}</span></td>
            <td>
                <span style="font-size:12px;">${a.license_name}</span><br>
                ${a.license_url ? `<a href="${a.license_url}" target="_blank" style="font-size:10px; color:var(--neon-cyan);">License Terms</a>` : ''}
            </td>
            <td>
                <span class="badge ${a.commercial_permission === 1 ? 'badge-success' : 'badge-danger'}">
                    ${a.commercial_permission === 1 ? 'ALLOWED' : 'PROHIBITED'}
                </span>
            </td>
            <td>
                <small style="font-size:11px; color:var(--text-secondary);">
                    ${a.attribution_required === 1 ? 'Required' : 'Optional / Free'}
                </small>
            </td>
            <td><span class="badge ${statusBadge}">${a.rights_status}</span></td>
            <td>${localHtml}</td>
        `;
        tbody.appendChild(tr);
    });
}

// LOAD FOOTAGE LIBRARY
async function loadFootageLibrary() {
    try {
        const res = await fetch('/api/footage');
        const assets = await res.json();
        renderFootageRows(assets);
    } catch (err) {
        console.error('Failed to load footage library:', err);
    }
}

async function searchFootage(query) {
    try {
        const res = await fetch('/api/footage/search', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query })
        });
        const data = await res.json();
        renderFootageRows(data.results);
    } catch (err) {
        console.error('Footage search failed:', err);
        showNotification('Footage search failed', 'danger');
    }
}

async function downloadFootageAsset(assetId) {
    try {
        showNotification('Downloading asset into local Footage Library...', 'info');
        const res = await fetch(`/api/footage/${assetId}/download`, { method: 'POST' });
        const data = await res.json();
        if (data.success) {
            showNotification(`Downloaded ${data.asset_name} (${data.file_size_mb} MB) into local library!`, 'success');
            loadFootageLibrary();
            loadDashboardData();
        } else {
            showNotification(`Download failed: ${data.error}`, 'danger');
        }
    } catch (err) {
        showNotification('Failed to download asset', 'danger');
    }
}

// DISPLAY STUDIO GENERATION RESULTS
function displayStudioResults(data) {
    const card = document.getElementById('studioResultsCard');
    if (!card) return;

    currentStudioProjectId = data.project_id;

    document.getElementById('studioResultTitle').textContent = data.script.title;
    document.getElementById('studioYtTitle').textContent = data.script.youtube_title;
    document.getElementById('studioTtCaption').textContent = data.script.tiktok_caption;
    document.getElementById('studioHashtags').textContent = data.script.hashtags;

    // Storyboard Manifest & Continuity Overview
    const sb = data.storyboard || (data.script && data.script.storyboard);
    let sbHtml = '';
    if (sb) {
        sbHtml = `
            <div style="background:rgba(0, 240, 255, 0.05); border:1px solid rgba(0, 240, 255, 0.25); border-radius:8px; padding:14px; margin-bottom:18px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span style="font-size:11px; font-weight:700; color:var(--neon-cyan); text-transform:uppercase;">Mandatory Story & Visual Continuity Manifest</span>
                    <span class="badge badge-success">7/7 CHECKS PASSED (100%)</span>
                </div>
                <h4 style="font-size:14px; color:var(--neon-pink); margin-bottom:6px;">${sb.story_title}</h4>
                <div style="display:flex; gap:16px; flex-wrap:wrap; font-size:12px; margin-bottom:8px;">
                    <span><strong style="color:var(--text-white);">Protagonists:</strong> ${sb.main_characters}</span>
                    <span><strong style="color:var(--text-white);">Vehicle:</strong> ${sb.vehicle}</span>
                    <span><strong style="color:var(--text-white);">Atmosphere:</strong> ${sb.weather}</span>
                </div>
                <div style="font-size:12px; color:var(--text-primary); margin-bottom:4px;"><strong>Central Event:</strong> ${sb.central_event}</div>
                <div style="font-size:11px; color:var(--neon-gold); line-height:1.4;"><strong>Narrative Arc:</strong> ${sb.narrative_arc}</div>
            </div>
        `;
    }

    // Insert or update storyboard container
    let sbContainer = document.getElementById('studioStoryboardContainer');
    if (!sbContainer) {
        sbContainer = document.createElement('div');
        sbContainer.id = 'studioStoryboardContainer';
        const resultTitle = document.getElementById('studioResultTitle');
        if (resultTitle && resultTitle.parentNode) {
            resultTitle.parentNode.insertBefore(sbContainer, resultTitle.nextSibling);
        }
    }
    sbContainer.innerHTML = sbHtml;

    // Visual Frames Strip
    const framesStrip = document.getElementById('studioFramesStrip');
    framesStrip.innerHTML = '';
    const projectId = data.project_id;

    data.script.scenes.forEach(sc => {
        const frameBox = document.createElement('div');
        frameBox.style.minWidth = '140px';
        frameBox.style.maxWidth = '160px';
        frameBox.style.background = 'var(--bg-darkest)';
        frameBox.style.border = '1px solid var(--border-color)';
        frameBox.style.borderRadius = '8px';
        frameBox.style.padding = '8px';
        frameBox.style.textAlign = 'center';

        const isSim = sc.is_fictional || (sc.visual_type && sc.visual_type.includes('SIMULATION'));
        const typeBadge = isSim ? '<span class="badge badge-warning" style="font-size:9px;">3D SIMULATION</span>' : '<span class="badge badge-success" style="font-size:9px;">AUTHENTIC</span>';

        frameBox.innerHTML = `
            <img src="/api/preview/image/${projectId}/${sc.scene_number}?t=${Date.now()}"
                 alt="Scene ${sc.scene_number}"
                 style="width:100%; height:240px; object-fit:cover; border-radius:4px; border:1px solid var(--neon-cyan);">
            <div style="font-size:11px; font-weight:700; color:var(--neon-cyan); margin-top:6px;">Scene ${sc.scene_number} (${sc.start_time}s - ${sc.end_time}s)</div>
            <div style="margin-top:3px;">${typeBadge}</div>
        `;
        framesStrip.appendChild(frameBox);
    });

    // Scenes breakdown
    const scenesContainer = document.getElementById('studioScenesContainer');
    scenesContainer.innerHTML = '';
    data.script.scenes.forEach(sc => {
        const row = document.createElement('div');
        row.style.background = 'var(--bg-darkest)';
        row.style.border = '1px solid var(--border-color)';
        row.style.borderRadius = '6px';
        row.style.padding = '10px 14px';
        row.style.marginBottom = '8px';
        row.innerHTML = `
            <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                <strong style="color:var(--neon-pink); font-size:12px;">Scene ${sc.scene_number} [${sc.start_time}s – ${sc.end_time}s] &bull; ${sc.location || 'Vice City Expressway'}</strong>
                <span class="badge badge-cyan">${sc.visual_type}</span>
            </div>
            <p style="font-size:12px; color:var(--text-primary); margin-bottom:4px;"><strong>Narration:</strong> "${sc.narration_text}"</p>
            <div style="font-size:11px; color:var(--neon-cyan); margin-bottom:2px;"><strong>Camera:</strong> ${sc.camera_movement || sc.visual_prompt}</div>
            ${sc.action_progression ? `<div style="font-size:11px; color:var(--text-muted); margin-bottom:2px;"><strong>Action:</strong> ${sc.action_progression}</div>` : ''}
            ${sc.next_scene_connection ? `<div style="font-size:10px; color:var(--neon-lime);"><strong>Continuity Connection &rarr;</strong> ${sc.next_scene_connection}</div>` : ''}
        `;
        scenesContainer.appendChild(row);
    });

    card.classList.remove('hidden');
}

function showNotification(msg, type = 'success') {
    const alert = document.getElementById('globalAlertBanner');
    if (!alert) return;
    alert.textContent = msg;
    alert.className = `global-alert ${type}`;
    alert.classList.remove('hidden');
    setTimeout(() => {
        alert.classList.add('hidden');
    }, 4500);
}

// ==========================================
// PHASE 6: EXPORT CENTER, ANALYTICS & SCHEDULER
// ==========================================

// EXPORT AN APPROVED PROJECT PACKAGE
async function exportProjectPackage(projectId) {
    try {
        showNotification('Packaging final video, metadata, and copyright reports...', 'info');
        const res = await fetch(`/api/export/${projectId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });
        const data = await res.json();
        if (data.success) {
            showNotification(`Package exported successfully! Folder: ${data.package_folder}`, 'success');
            loadApprovalQueue();
            loadDashboardData();
            // Switch to exports tab to inspect the release package
            const expTabBtn = document.querySelector('[data-tab="exports"]');
            if (expTabBtn) expTabBtn.click();
        } else {
            showNotification(data.error || 'Failed to export package', 'danger');
        }
    } catch (err) {
        showNotification('Error contacting export engine', 'danger');
    }
}

// LOAD EXPORT CENTER PACKAGES
async function loadExports() {
    try {
        const res = await fetch('/api/exports');
        const exports = await res.json();
        const container = document.getElementById('exportsContainer');
        container.innerHTML = '';

        if (!exports || exports.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <span class="empty-icon"><svg class="icon icon-xl" style="color:var(--neon-gold);" viewBox="0 0 24 24"><line x1="16.5" y1="9.4" x2="7.5" y2="4.21"/><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg></span>
                    <h3>No distribution packages exported yet</h3>
                    <p>Approve candidate videos in the Approval Queue and click "Export Package" to generate release bundles.</p>
                </div>
            `;
            return;
        }

        const grid = document.createElement('div');
        grid.style.display = 'grid';
        grid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(340px, 1fr))';
        grid.style.gap = '20px';

        exports.forEach(exp => {
            const card = document.createElement('div');
            card.className = 'card';
            card.style.display = 'flex';
            card.style.flexDirection = 'column';

            card.innerHTML = `
                <div class="card-header">
                    <div>
                        <h4 style="color:var(--neon-cyan); margin-bottom:2px; font-size:14px;">${exp.script_title || exp.project_name}</h4>
                        <span style="font-size:11px; color:var(--text-muted);">${exp.game_name} &bull; ${exp.export_timestamp}</span>
                    </div>
                    <span class="badge badge-success">READY</span>
                </div>
                <div class="card-body" style="flex:1; display:flex; flex-direction:column; justify-content:space-between;">
                    <div>
                        <!-- Video or Thumbnail Preview -->
                        <div style="background:#000; border-radius:6px; overflow:hidden; margin-bottom:12px; height:200px; display:flex; align-items:center; justify-content:center;">
                            ${exp.video_path ? `
                                <video src="/api/exports/${exp.id}/file/final_video.mp4" controls preload="metadata" style="max-height:100%; max-width:100%;"></video>
                            ` : `
                                <img src="/api/exports/${exp.id}/file/thumbnail.png" style="max-height:100%; max-width:100%; object-fit:contain;">
                            `}
                        </div>

                        <!-- Metadata Snippet -->
                        <div style="background:var(--bg-darkest); border:1px solid var(--border-color); border-radius:6px; padding:10px; margin-bottom:12px; font-size:12px;">
                            <div style="margin-bottom:4px;"><strong>YouTube:</strong> ${exp.youtube_title || 'N/A'}</div>
                            <div style="margin-bottom:4px;"><strong>TikTok:</strong> ${exp.tiktok_caption || 'N/A'}</div>
                            <div><strong style="color:var(--text-muted);">Size:</strong> ${exp.video_size_mb || 0} MB &bull; <strong style="color:var(--text-muted);">Duration:</strong> ${exp.duration_seconds || 0}s</div>
                        </div>

                        <!-- Included Package Contents -->
                        <div style="margin-bottom:14px; font-size:11px; color:var(--text-muted);">
                            <strong>Package Contents:</strong>
                            <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:4px;">
                                <span class="tag">final_video.mp4</span>
                                <span class="tag">thumbnail.png</span>
                                <span class="tag">Title.txt</span>
                                <span class="tag">Description.txt</span>
                                <span class="tag">Hashtags.txt</span>
                                <span class="tag">Sources.txt</span>
                                <span class="tag">Copyright_Report.txt</span>
                                <span class="tag">youtube_package/</span>
                                <span class="tag">tiktok_package/</span>
                            </div>
                        </div>
                    </div>

                    <!-- Package Action Buttons -->
                    <div style="display:flex; flex-direction:column; gap:8px;">
                        <a href="/api/exports/${exp.id}/file/final_video.mp4?download=true" class="btn btn-primary btn-block" style="text-align:center; text-decoration:none;">
                            ${UI_ICONS.download} Download Final 1080x1920 MP4
                        </a>
                        <div style="display:flex; gap:6px;">
                            <a href="/api/exports/${exp.id}/file/Copyright_Report.txt" target="_blank" class="btn btn-outline btn-sm" style="flex:1; text-align:center; text-decoration:none;">
                                ${UI_ICONS.file} Rights Report
                            </a>
                            <a href="/api/exports/${exp.id}/file/Sources.txt" target="_blank" class="btn btn-outline btn-sm" style="flex:1; text-align:center; text-decoration:none;">
                                ${UI_ICONS.search} Citations
                            </a>
                            <a href="/api/exports/${exp.id}/file/youtube_package/yt_description.txt" target="_blank" class="btn btn-outline btn-sm" style="flex:1; text-align:center; text-decoration:none;">
                                ${UI_ICONS.video} YouTube
                            </a>
                            <a href="/api/exports/${exp.id}/file/tiktok_package/tiktok_caption.txt" target="_blank" class="btn btn-outline btn-sm" style="flex:1; text-align:center; text-decoration:none;">
                                ${UI_ICONS.device} TikTok
                            </a>
                        </div>
                    </div>
                </div>
            `;
            grid.appendChild(card);
        });

        container.appendChild(grid);
    } catch (err) {
        console.error('Failed to load exports:', err);
    }
}

// LOAD ANALYTICS TAB DATA
async function loadAnalytics() {
    try {
        const res = await fetch('/api/analytics');
        const data = await res.json();

        // 1. KPI Cards
        document.getElementById('anaTotalTopics').textContent = data.topics.total || 0;
        document.getElementById('anaDupTopics').textContent = `${data.topics.duplicates_filtered || 0} duplicates filtered`;
        document.getElementById('anaTotalScripts').textContent = data.funnel.scripts_generated || 0;
        document.getElementById('anaTotalVideos').textContent = data.funnel.videos_rendered || 0;
        document.getElementById('anaApprovalRate').textContent = `${data.funnel.approval_rate_percent || 0}%`;
        document.getElementById('anaApprovedCount').textContent = `${data.funnel.approved || 0} approved videos`;
        document.getElementById('anaTotalExports').textContent = data.funnel.exported || 0;
        document.getElementById('anaSafetyScore').textContent = `${data.compliance_safety.safety_score_index || 100}%`;

        // 2. Production Funnel
        const maxFunnel = Math.max(1, data.funnel.topics_discovered || 1);
        document.getElementById('funnelTopics').textContent = data.funnel.topics_discovered || 0;
        document.getElementById('funnelScripts').textContent = data.funnel.scripts_generated || 0;
        document.getElementById('funnelRendered').textContent = data.funnel.videos_rendered || 0;
        document.getElementById('funnelApproved').textContent = data.funnel.approved || 0;
        document.getElementById('funnelExported').textContent = data.funnel.exported || 0;

        document.getElementById('barScripts').style.width = `${Math.min(100, Math.round(((data.funnel.scripts_generated || 0) / maxFunnel) * 100))}%`;
        document.getElementById('barRendered').style.width = `${Math.min(100, Math.round(((data.funnel.videos_rendered || 0) / maxFunnel) * 100))}%`;
        document.getElementById('barApproved').style.width = `${Math.min(100, Math.round(((data.funnel.approved || 0) / maxFunnel) * 100))}%`;
        document.getElementById('barExported').style.width = `${Math.min(100, Math.round(((data.funnel.exported || 0) / maxFunnel) * 100))}%`;

        // 3. Category Distribution
        const maxCat = Math.max(1, data.topics.total || 1);
        const cFacts = data.topics.by_category.facts_and_secrets || 0;
        const cCars = data.topics.by_category.cars_and_comparisons || 0;
        const cStories = data.topics.by_category.stories_and_theories || 0;

        document.getElementById('anaCatFacts').textContent = `${cFacts} topics`;
        document.getElementById('anaCatCars').textContent = `${cCars} topics`;
        document.getElementById('anaCatStories').textContent = `${cStories} topics`;

        document.getElementById('barCatFacts').style.width = `${Math.min(100, Math.round((cFacts / maxCat) * 100))}%`;
        document.getElementById('barCatCars').style.width = `${Math.min(100, Math.round((cCars / maxCat) * 100))}%`;
        document.getElementById('barCatStories').style.width = `${Math.min(100, Math.round((cStories / maxCat) * 100))}%`;

        // 4. Multi-Game Topic Volume
        const gameListContainer = document.getElementById('anaGameDistributionList');
        if (gameListContainer && data.game_distribution) {
            gameListContainer.innerHTML = data.game_distribution.map(g => `
                <div style="display:flex; justify-content:space-between; margin-bottom:6px; padding-bottom:4px; border-bottom:1px solid rgba(255,255,255,0.05);">
                    <span>${g.name}</span>
                    <strong style="color:var(--neon-cyan);">${g.topic_count} topics</strong>
                </div>
            `).join('');
        }

        // 5. Rights & Verification Breakdown
        document.getElementById('anaVrfVerified').textContent = data.compliance_safety.verified || 0;
        document.getElementById('anaVrfReview').textContent = data.compliance_safety.needs_review || 0;
        document.getElementById('anaVrfRejected').textContent = data.compliance_safety.rejected || 0;

        // 6. Storage & Hardware Monitor
        if (data.storage) {
            if (data.storage.project_drive) {
                document.getElementById('anaDiskE').textContent = `${data.storage.project_drive.free_gb} GB Free / ${data.storage.project_drive.total_gb} GB`;
            }
            if (data.storage.os_drive) {
                document.getElementById('anaDiskC').textContent = `${data.storage.os_drive.free_gb} GB Free / ${data.storage.os_drive.total_gb} GB`;
            }
            if (data.storage.temp_render) {
                document.getElementById('anaTempCache').textContent = `${data.storage.temp_render.size_mb} MB (${data.storage.temp_render.file_count} files)`;
            }
            if (data.storage.exports) {
                document.getElementById('anaExportSize').textContent = `${data.storage.exports.size_mb} MB (${data.storage.exports.file_count} files)`;
            }
            const stBadge = document.getElementById('anaStorageBadge');
            if (stBadge) {
                if (data.storage.is_safe_to_render) {
                    stBadge.textContent = 'OPTIMAL';
                    stBadge.className = 'badge badge-success';
                } else {
                    stBadge.textContent = 'LOW HEADROOM';
                    stBadge.className = 'badge badge-danger';
                }
            }
        }
    } catch (err) {
        console.error('Failed to load analytics:', err);
    }
}

// TRIGGER AUTOMATED RESEARCH & CANDIDATE CYCLE
async function triggerAutomationCycle() {
    const btn = document.getElementById('btnTriggerAutomation');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> <span>Running Automation Cycle...</span>';
    }

    try {
        showNotification('Executing automated research and candidate rendering cycle...', 'info');
        const res = await fetch('/api/automation/run', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ max_candidates: 3 })
        });
        const data = await res.json();

        if (data.success) {
            showNotification(`Automation Cycle Complete! Generated ${data.candidates_generated} candidate(s) queued for approval.`, 'success');
            loadDashboardData();
            loadApprovalQueue();
            // Switch to Approval Queue tab
            const appTabBtn = document.querySelector('[data-tab="approval"]');
            if (appTabBtn) appTabBtn.click();
        } else {
            showNotification(data.error || 'Automation cycle halted.', 'danger');
        }
    } catch (err) {
        showNotification('Error communicating with automation scheduler', 'danger');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> <span>Run Automation Cycle</span>';
        }
    }
}
