# HomeGroup - Implementation Specification
## 4 Major Feature Categories Enhancement

This document specifies the implementation details for adding 465+ features across 4 major categories.

---

## IMPLEMENTATION APPROACH

Due to the size and complexity, we'll implement in phases:

### Phase 1: UI/UX Foundation (Complete Theme System)
### Phase 2: Data Management Core (Search & Custom Fields)
### Phase 3: Analytics Engine (Health Scores & Predictions)
### Phase 4: Reporting Framework (Custom Reports & PDFs)

Each phase will be fully functional before moving to the next.

---

## CATEGORY 1: UI/UX IMPROVEMENTS

### 1.1 Theme System (Dark Mode, Multiple Themes)

**CSS Variables to Add:**
```css
:root {
    /* Theme: Light (Default - keeping existing colors) */
    --bg-primary: #2c3e50;
    --bg-secondary: #34495e;
    --bg-tertiary: #2c3e50;
    --text-primary: #ecf0f1;
    --text-secondary: #bdc3c7;
    --accent-primary: #3498db;
    --accent-secondary: #2980b9;
    --border-color: #7f8c8d;
    --success-color: #2ecc71;
    --error-color: #e74c3c;
    --warning-color: #f39c12;
    --info-color: #3498db;
}

[data-theme="dark"] {
    --bg-primary: #1a1a1a;
    --bg-secondary: #2d2d2d;
    --bg-tertiary: #1a1a1a;
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
    --accent-primary: #3498db;
    --accent-secondary: #2980b9;
    --border-color: #444444;
    --success-color: #27ae60;
    --error-color: #c0392b;
    --warning-color: #d68910;
    --info-color: #2980b9;
}

[data-theme="light"] {
    --bg-primary: #ffffff;
    --bg-secondary: #f8f9fa;
    --bg-tertiary: #e9ecef;
    --text-primary: #212529;
    --text-secondary: #6c757d;
    --accent-primary: #007bff;
    --accent-secondary: #0056b3;
    --border-color: #dee2e6;
    --success-color: #28a745;
    --error-color: #dc3545;
    --warning-color: #ffc107;
    --info-color: #17a2b8;
}

[data-theme="high-contrast"] {
    --bg-primary: #000000;
    --bg-secondary: #1a1a1a;
    --bg-tertiary: #000000;
    --text-primary: #ffffff;
    --text-secondary: #ffffff;
    --accent-primary: #ffff00;
    --accent-secondary: #ffff00;
    --border-color: #ffffff;
    --success-color: #00ff00;
    --error-color: #ff0000;
    --warning-color: #ffff00;
    --info-color: #00ffff;
}
```

**JavaScript Functions to Add:**
```javascript
// Theme Management
const ThemeManager = {
    themes: ['default', 'dark', 'light', 'high-contrast'],

    init() {
        const savedTheme = localStorage.getItem('theme') || 'default';
        this.setTheme(savedTheme);
    },

    setTheme(themeName) {
        document.documentElement.setAttribute('data-theme', themeName);
        localStorage.setItem('theme', themeName);
        this.updateThemeUI();
    },

    toggleTheme() {
        const currentIndex = this.themes.indexOf(this.getCurrentTheme());
        const nextIndex = (currentIndex + 1) % this.themes.length;
        this.setTheme(this.themes[nextIndex]);
    },

    getCurrentTheme() {
        return document.documentElement.getAttribute('data-theme') || 'default';
    },

    updateThemeUI() {
        const selector = document.getElementById('theme-selector');
        if (selector) {
            selector.value = this.getCurrentTheme();
        }
    }
};
```

### 1.2 Smooth Animations & Transitions

**CSS to Add:**
```css
/* Smooth Transitions */
* {
    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

/* Page Transitions */
section {
    animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Button Hover Effects */
.btn {
    position: relative;
    overflow: hidden;
}

.btn::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.btn:hover::before {
    width: 300px;
    height: 300px;
}

/* Card Hover Effects */
.box {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.box:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.3);
}

/* Loading Spinner */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.loading-spinner {
    border: 4px solid var(--border-color);
    border-top: 4px solid var(--accent-primary);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
    margin: 20px auto;
}

/* Skeleton Screen */
.skeleton {
    background: linear-gradient(90deg, var(--bg-secondary) 25%, var(--bg-tertiary) 50%, var(--bg-secondary) 75%);
    background-size: 200% 100%;
    animation: loading 1.5s ease-in-out infinite;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

.skeleton-text {
    height: 1em;
    margin-bottom: 0.5em;
    border-radius: 4px;
}

.skeleton-box {
    height: 200px;
    border-radius: 6px;
}
```

### 1.3 Loading Indicators & Progress

**HTML Components to Add:**
```html
<!-- Global Loading Overlay -->
<div id="global-loading" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); z-index: 10000; display: flex; align-items: center; justify-content: center; flex-direction: column;">
    <div class="loading-spinner"></div>
    <p style="color: white; margin-top: 1rem;">Loading...</p>
</div>

<!-- Progress Bar -->
<div id="progress-bar" style="position: fixed; top: 0; left: 0; right: 0; height: 3px; background: var(--accent-primary); transform: scaleX(0); transform-origin: left; transition: transform 0.3s ease; z-index: 9999;"></div>
```

**JavaScript Functions:**
```javascript
const LoadingManager = {
    show(message = 'Loading...') {
        const overlay = document.getElementById('global-loading');
        if (overlay) {
            overlay.querySelector('p').textContent = message;
            overlay.style.display = 'flex';
        }
    },

    hide() {
        const overlay = document.getElementById('global-loading');
        if (overlay) {
            overlay.style.display = 'none';
        }
    },

    setProgress(percent) {
        const bar = document.getElementById('progress-bar');
        if (bar) {
            bar.style.transform = `scaleX(${percent / 100})`;
            if (percent >= 100) {
                setTimeout(() => bar.style.transform = 'scaleX(0)', 300);
            }
        }
    }
};
```

### 1.4 Enhanced Tooltips

**CSS:**
```css
.tooltip-trigger {
    position: relative;
    cursor: help;
}

.tooltip-content {
    visibility: hidden;
    position: absolute;
    z-index: 1000;
    background: var(--bg-secondary);
    color: var(--text-primary);
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 0.85rem;
    white-space: nowrap;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    opacity: 0;
    transition: opacity 0.3s, visibility 0.3s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    border: 1px solid var(--border-color);
}

.tooltip-content::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    border: 5px solid transparent;
    border-top-color: var(--bg-secondary);
}

.tooltip-trigger:hover .tooltip-content {
    visibility: visible;
    opacity: 1;
}
```

**JavaScript:**
```javascript
const TooltipManager = {
    init() {
        // Auto-add tooltips to elements with title attribute
        document.querySelectorAll('[title]').forEach(el => {
            if (!el.classList.contains('tooltip-trigger')) {
                this.addTooltip(el, el.getAttribute('title'));
                el.removeAttribute('title');
            }
        });
    },

    addTooltip(element, text) {
        element.classList.add('tooltip-trigger');
        const tooltip = document.createElement('span');
        tooltip.className = 'tooltip-content';
        tooltip.textContent = text;
        element.appendChild(tooltip);
    }
};
```

### 1.5 Responsive Design Improvements

**CSS Enhancements:**
```css
/* Mobile-First Improvements */
@media (max-width: 480px) {
    body {
        font-size: 14px;
    }

    .box {
        padding: 0.75rem;
    }

    .btn {
        padding: 0.5rem 0.75rem;
        font-size: 0.8rem;
    }

    nav {
        flex-direction: column;
        align-items: flex-start;
    }

    nav ul {
        width: 100%;
        flex-direction: column;
        gap: 0.25rem;
    }

    table {
        font-size: 0.75rem;
    }
}

/* Tablet Optimizations */
@media (min-width: 768px) and (max-width: 1024px) {
    .grid-cols-2 {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Touch-Friendly */
@media (pointer: coarse) {
    .btn, button, a {
        min-height: 44px;
        min-width: 44px;
        padding: 0.75rem 1rem;
    }

    input, select, textarea {
        font-size: 16px !important; /* Prevent zoom on iOS */
    }
}
```

---

## CATEGORY 2: DATA MANAGEMENT

### 2.1 Universal Search

**HTML Section to Add:**
```html
<section id="universal-search-section">
    <h2><i class="fas fa-search"></i> Universal Search</h2>
    <div class="box">
        <div class="form-group">
            <label for="universal-search-input">Search Across All Data</label>
            <input type="text" id="universal-search-input" placeholder="Search members, events, GC items, finances..." />
        </div>
        <div class="form-group">
            <label>Search In:</label>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                <label><input type="checkbox" checked data-search-type="members"> Members</label>
                <label><input type="checkbox" checked data-search-type="events"> Events</label>
                <label><input type="checkbox" checked data-search-type="gc"> Group Conscience</label>
                <label><input type="checkbox" checked data-search-type="finances"> Finances</label>
                <label><input type="checkbox" checked data-search-type="literature"> Literature</label>
                <label><input type="checkbox" checked data-search-type="service"> Service Positions</label>
            </div>
        </div>
        <button class="btn" onclick="performUniversalSearch()"><i class="fas fa-search"></i> Search</button>
    </div>

    <div id="universal-search-results" class="mt-4"></div>
</section>
```

**JavaScript Functions:**
```javascript
const UniversalSearch = {
    search(query, types) {
        const results = [];
        query = query.toLowerCase();

        if (types.includes('members')) {
            const members = storage.getMembers();
            members.forEach(m => {
                if (m.name.toLowerCase().includes(query) ||
                    (m.email && m.email.toLowerCase().includes(query)) ||
                    (m.phone && m.phone.includes(query))) {
                    results.push({
                        type: 'Member',
                        title: m.name,
                        subtitle: m.email || m.phone,
                        data: m,
                        section: 'roster-section'
                    });
                }
            });
        }

        if (types.includes('events')) {
            const events = storage.getEvents();
            events.forEach(e => {
                if (e.title.toLowerCase().includes(query) ||
                    (e.location && e.location.toLowerCase().includes(query))) {
                    results.push({
                        type: 'Event',
                        title: e.title,
                        subtitle: e.date || e.dayOfWeek,
                        data: e,
                        section: 'schedule-section'
                    });
                }
            });
        }

        if (types.includes('gc')) {
            const gcItems = storage.getGroupConscienceLog();
            gcItems.forEach(item => {
                if (item.title.toLowerCase().includes(query) ||
                    (item.description && item.description.toLowerCase().includes(query))) {
                    results.push({
                        type: 'GC Item',
                        title: item.title,
                        subtitle: item.date + ' - ' + item.status,
                        data: item,
                        section: 'gc-history-section'
                    });
                }
            });
        }

        if (types.includes('finances')) {
            const expenses = storage.getExpenses();
            expenses.forEach(exp => {
                if (exp.description.toLowerCase().includes(query) ||
                    exp.category.toLowerCase().includes(query)) {
                    results.push({
                        type: 'Expense',
                        title: exp.description,
                        subtitle: '$' + exp.amount + ' - ' + exp.category,
                        data: exp,
                        section: 'finance-section'
                    });
                }
            });
        }

        if (types.includes('literature')) {
            const lit = storage.getLiteratureInventory();
            lit.forEach(item => {
                if (item.title.toLowerCase().includes(query)) {
                    results.push({
                        type: 'Literature',
                        title: item.title,
                        subtitle: 'Stock: ' + item.quantity,
                        data: item,
                        section: 'literature-section'
                    });
                }
            });
        }

        if (types.includes('service')) {
            const positions = storage.getServicePositions();
            positions.forEach(pos => {
                if (pos.position.toLowerCase().includes(query) ||
                    (pos.member && pos.member.toLowerCase().includes(query))) {
                    results.push({
                        type: 'Service Position',
                        title: pos.position,
                        subtitle: pos.member || 'Vacant',
                        data: pos,
                        section: 'service-positions-section'
                    });
                }
            });
        }

        return results;
    },

    displayResults(results) {
        const container = document.getElementById('universal-search-results');
        if (results.length === 0) {
            container.innerHTML = '<div class="box"><p>No results found</p></div>';
            return;
        }

        let html = `<h3>Found ${results.length} results</h3>`;

        // Group by type
        const grouped = {};
        results.forEach(r => {
            if (!grouped[r.type]) grouped[r.type] = [];
            grouped[r.type].push(r);
        });

        Object.keys(grouped).forEach(type => {
            html += `<div class="box mt-4">
                <h4>${type} (${grouped[type].length})</h4>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">`;

            grouped[type].forEach(item => {
                html += `
                    <div style="padding: 0.75rem; background: var(--bg-tertiary); border-radius: 4px; cursor: pointer;" onclick="goToSection('${item.section}')">
                        <div style="font-weight: bold;">${sanitizeInput(item.title)}</div>
                        <div style="font-size: 0.85rem; opacity: 0.8;">${sanitizeInput(item.subtitle)}</div>
                    </div>
                `;
            });

            html += `</div></div>`;
        });

        container.innerHTML = html;
    }
};

function performUniversalSearch() {
    const query = document.getElementById('universal-search-input').value.trim();
    if (!query) {
        showToast('Please enter a search term', 'error');
        return;
    }

    const types = [];
    document.querySelectorAll('[data-search-type]:checked').forEach(cb => {
        types.push(cb.getAttribute('data-search-type'));
    });

    LoadingManager.show('Searching...');

    setTimeout(() => {
        const results = UniversalSearch.search(query, types);
        UniversalSearch.displayResults(results);
        LoadingManager.hide();
        showToast(`Found ${results.length} results`, 'success');
    }, 300);
}
```

### 2.2 Custom Fields System

**Storage Functions to Add:**
```javascript
getCustomFields() {
    try { return JSON.parse(localStorage.getItem('customFields') || '{}'); }
    catch(e) { console.error('Error parsing customFields:', e); return {}; }
},
saveCustomFields(fields) { safeStorageSave('customFields', fields); }
```

**HTML Section:**
```html
<section id="custom-fields-section">
    <h2><i class="fas fa-cogs"></i> Custom Fields Manager</h2>
    <p class="mb-4">Add custom fields to members, events, or any data type.</p>

    <div class="box">
        <h3>Add Custom Field</h3>
        <div class="form-group">
            <label>Apply To:</label>
            <select id="custom-field-entity">
                <option value="members">Members</option>
                <option value="events">Events</option>
                <option value="service">Service Positions</option>
                <option value="gc">GC Items</option>
            </select>
        </div>
        <div class="form-group">
            <label>Field Name:</label>
            <input type="text" id="custom-field-name" placeholder="e.g., T-Shirt Size" />
        </div>
        <div class="form-group">
            <label>Field Type:</label>
            <select id="custom-field-type">
                <option value="text">Text</option>
                <option value="number">Number</option>
                <option value="date">Date</option>
                <option value="select">Dropdown</option>
                <option value="checkbox">Checkbox</option>
                <option value="textarea">Long Text</option>
            </select>
        </div>
        <div class="form-group" id="custom-field-options-group" style="display: none;">
            <label>Options (comma-separated):</label>
            <input type="text" id="custom-field-options" placeholder="e.g., Small, Medium, Large, XL" />
        </div>
        <button class="btn" onclick="addCustomField()"><i class="fas fa-plus"></i> Add Field</button>
    </div>

    <div class="box mt-4">
        <h3>Active Custom Fields</h3>
        <div id="custom-fields-list"></div>
    </div>
</section>
```

**JavaScript:**
```javascript
const CustomFields = {
    add(entity, field) {
        const fields = storage.getCustomFields();
        if (!fields[entity]) fields[entity] = [];

        fields[entity].push({
            id: genId(),
            name: field.name,
            type: field.type,
            options: field.options || [],
            required: field.required || false
        });

        storage.saveCustomFields(fields);
        this.refresh();
        showToast('Custom field added', 'success');
    },

    remove(entity, fieldId) {
        const fields = storage.getCustomFields();
        if (fields[entity]) {
            fields[entity] = fields[entity].filter(f => f.id !== fieldId);
            storage.saveCustomFields(fields);
            this.refresh();
            showToast('Custom field removed', 'success');
        }
    },

    get(entity) {
        const fields = storage.getCustomFields();
        return fields[entity] || [];
    },

    refresh() {
        const fields = storage.getCustomFields();
        const container = document.getElementById('custom-fields-list');
        if (!container) return;

        let html = '';
        Object.keys(fields).forEach(entity => {
            if (fields[entity].length > 0) {
                html += `<h4>${entity.charAt(0).toUpperCase() + entity.slice(1)}</h4>`;
                fields[entity].forEach(field => {
                    html += `
                        <div style="padding: 0.5rem; background: var(--bg-tertiary); border-radius: 4px; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <strong>${sanitizeInput(field.name)}</strong>
                                <span style="opacity: 0.7; margin-left: 0.5rem;">(${field.type})</span>
                            </div>
                            <button class="btn secondary" onclick="CustomFields.remove('${entity}', '${field.id}')">Delete</button>
                        </div>
                    `;
                });
            }
        });

        container.innerHTML = html || '<p>No custom fields defined</p>';
    },

    renderInput(field, value = '') {
        let html = `<div class="form-group">
            <label>${sanitizeInput(field.name)}${field.required ? ' *' : ''}</label>`;

        switch (field.type) {
            case 'text':
                html += `<input type="text" id="custom-${field.id}" value="${sanitizeInput(value)}" />`;
                break;
            case 'number':
                html += `<input type="number" id="custom-${field.id}" value="${value}" />`;
                break;
            case 'date':
                html += `<input type="date" id="custom-${field.id}" value="${value}" />`;
                break;
            case 'select':
                html += `<select id="custom-${field.id}">`;
                field.options.forEach(opt => {
                    html += `<option value="${sanitizeInput(opt)}" ${value === opt ? 'selected' : ''}>${sanitizeInput(opt)}</option>`;
                });
                html += `</select>`;
                break;
            case 'checkbox':
                html += `<input type="checkbox" id="custom-${field.id}" ${value ? 'checked' : ''} />`;
                break;
            case 'textarea':
                html += `<textarea id="custom-${field.id}" rows="3">${sanitizeInput(value)}</textarea>`;
                break;
        }

        html += `</div>`;
        return html;
    }
};

function addCustomField() {
    const entity = document.getElementById('custom-field-entity').value;
    const name = document.getElementById('custom-field-name').value.trim();
    const type = document.getElementById('custom-field-type').value;
    const options = document.getElementById('custom-field-options').value.split(',').map(o => o.trim()).filter(o => o);

    if (!name) {
        showToast('Please enter a field name', 'error');
        return;
    }

    CustomFields.add(entity, { name, type, options });

    document.getElementById('custom-field-name').value = '';
    document.getElementById('custom-field-options').value = '';
}

document.addEventListener('DOMContentLoaded', () => {
    const typeSelect = document.getElementById('custom-field-type');
    if (typeSelect) {
        typeSelect.addEventListener('change', (e) => {
            const optionsGroup = document.getElementById('custom-field-options-group');
            optionsGroup.style.display = e.target.value === 'select' ? 'block' : 'none';
        });
    }
});
```

---

## CATEGORY 3: ANALYTICS & CHARTS

### 3.1 Group Health Score

**JavaScript:**
```javascript
const GroupHealthScore = {
    calculate() {
        const metrics = {
            financial: this.calculateFinancialHealth(),
            attendance: this.calculateAttendanceHealth(),
            service: this.calculateServiceHealth(),
            newcomer: this.calculateNewcomerHealth(),
            participation: this.calculateParticipationHealth()
        };

        const weights = {
            financial: 0.25,
            attendance: 0.25,
            service: 0.20,
            newcomer: 0.15,
            participation: 0.15
        };

        let totalScore = 0;
        Object.keys(metrics).forEach(key => {
            totalScore += metrics[key] * weights[key];
        });

        return {
            overall: Math.round(totalScore),
            metrics: metrics,
            grade: this.getGrade(totalScore),
            recommendations: this.getRecommendations(metrics)
        };
    },

    calculateFinancialHealth() {
        // Based on prudent reserve, contribution trends, expense management
        const reserve = storage.getPrudentReserve();
        const expenses = storage.getExpenses();
        const contributions = storage.getContributions();

        let score = 50; // Base score

        // Reserve health (0-30 points)
        if (reserve.currentBalance >= reserve.targetAmount) {
            score += 30;
        } else if (reserve.currentBalance >= reserve.targetAmount * 0.75) {
            score += 20;
        } else if (reserve.currentBalance >= reserve.targetAmount * 0.5) {
            score += 10;
        }

        // Contribution trend (0-20 points)
        if (contributions.length >= 3) {
            const recent3 = contributions.slice(-3).reduce((sum, c) => sum + c.amount, 0) / 3;
            const previous3 = contributions.slice(-6, -3).reduce((sum, c) => sum + c.amount, 0) / 3;
            if (recent3 > previous3) score += 20;
            else if (recent3 > previous3 * 0.9) score += 10;
        }

        return Math.min(100, score);
    },

    calculateAttendanceHealth() {
        const attendance = storage.getAttendanceRecords();
        if (attendance.length < 4) return 50;

        let score = 50;

        // Trend analysis (0-30 points)
        const recent4 = attendance.slice(-4);
        const avgRecent = recent4.reduce((sum, a) => sum + a.count, 0) / 4;
        const previous4 = attendance.slice(-8, -4);
        const avgPrevious = previous4.length > 0 ? previous4.reduce((sum, a) => sum + a.count, 0) / 4 : avgRecent;

        if (avgRecent > avgPrevious) score += 30;
        else if (avgRecent > avgPrevious * 0.9) score += 15;

        // Consistency (0-20 points)
        const variance = this.calculateVariance(recent4.map(a => a.count));
        if (variance < 5) score += 20;
        else if (variance < 10) score += 10;

        return Math.min(100, score);
    },

    calculateServiceHealth() {
        const positions = storage.getServicePositions();
        if (positions.length === 0) return 50;

        const filled = positions.filter(p => p.member).length;
        const fillRate = (filled / positions.length) * 100;

        return Math.round(fillRate);
    },

    calculateNewcomerHealth() {
        const newcomers = storage.getNewcomers();
        if (newcomers.length === 0) return 50;

        // Calculate retention rate
        const total = newcomers.length;
        const retained = newcomers.filter(n => {
            const meetings = n.meetings || 0;
            return meetings >= 10; // Consider retained if 10+ meetings
        }).length;

        return Math.round((retained / total) * 100);
    },

    calculateParticipationHealth() {
        const gcLog = storage.getGroupConscienceLog();
        if (gcLog.length === 0) return 50;

        // Based on GC participation and voting
        const recentGC = gcLog.slice(-5);
        const avgVotes = recentGC.reduce((sum, gc) => {
            const total = (gc.votesFor || 0) + (gc.votesAgainst || 0) + (gc.votesAbstain || 0);
            return sum + total;
        }, 0) / recentGC.length;

        // Assuming 20 members, 60%+ participation is excellent
        const members = storage.getMembers().length;
        const participationRate = (avgVotes / members) * 100;

        if (participationRate >= 60) return 100;
        if (participationRate >= 40) return 75;
        if (participationRate >= 20) return 50;
        return 25;
    },

    calculateVariance(numbers) {
        const avg = numbers.reduce((sum, n) => sum + n, 0) / numbers.length;
        const variance = numbers.reduce((sum, n) => sum + Math.pow(n - avg, 2), 0) / numbers.length;
        return Math.sqrt(variance);
    },

    getGrade(score) {
        if (score >= 90) return 'A';
        if (score >= 80) return 'B';
        if (score >= 70) return 'C';
        if (score >= 60) return 'D';
        return 'F';
    },

    getRecommendations(metrics) {
        const recommendations = [];

        if (metrics.financial < 70) {
            recommendations.push('Focus on building prudent reserve through 7th tradition education');
        }
        if (metrics.attendance < 70) {
            recommendations.push('Consider outreach efforts and meeting format variety to boost attendance');
        }
        if (metrics.service < 70) {
            recommendations.push('Hold service workshop to fill vacant positions');
        }
        if (metrics.newcomer < 70) {
            recommendations.push('Strengthen newcomer retention with buddy system and welcome packets');
        }
        if (metrics.participation < 70) {
            recommendations.push('Increase group conscience participation through education');
        }

        return recommendations;
    }
};
```

---

## CATEGORY 4: REPORTING

### 4.1 Custom Report Builder

**HTML:**
```html
<section id="custom-reports-section">
    <h2><i class="fas fa-file-alt"></i> Custom Report Builder</h2>
    <p class="mb-4">Build custom reports with any combination of data and filters.</p>

    <div class="box">
        <h3>Build New Report</h3>
        <div class="form-group">
            <label>Report Name:</label>
            <input type="text" id="report-name" placeholder="e.g., Monthly Summary" />
        </div>
        <div class="form-group">
            <label>Include Data:</label>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                <label><input type="checkbox" data-report-data="members"> Members</label>
                <label><input type="checkbox" data-report-data="attendance"> Attendance</label>
                <label><input type="checkbox" data-report-data="finances"> Finances</label>
                <label><input type="checkbox" data-report-data="gc"> Group Conscience</label>
                <label><input type="checkbox" data-report-data="service"> Service Positions</label>
                <label><input type="checkbox" data-report-data="literature"> Literature</label>
            </div>
        </div>
        <div class="form-group">
            <label>Date Range:</label>
            <input type="date" id="report-start-date" style="width: auto;" />
            to
            <input type="date" id="report-end-date" style="width: auto;" />
        </div>
        <button class="btn" onclick="generateCustomReport()"><i class="fas fa-file-pdf"></i> Generate Report (PDF)</button>
        <button class="btn secondary" onclick="previewCustomReport()"><i class="fas fa-eye"></i> Preview</button>
    </div>

    <div id="report-preview" class="mt-4"></div>
</section>
```

**JavaScript:**
```javascript
const CustomReportBuilder = {
    generate(config) {
        const data = this.gatherData(config);
        return this.formatReport(data, config);
    },

    gatherData(config) {
        const result = {};

        if (config.dataTypes.includes('members')) {
            result.members = storage.getMembers();
        }
        if (config.dataTypes.includes('attendance')) {
            result.attendance = this.filterByDate(storage.getAttendanceRecords(), config.startDate, config.endDate);
        }
        if (config.dataTypes.includes('finances')) {
            const expenses = this.filterByDate(storage.getExpenses(), config.startDate, config.endDate);
            const contributions = this.filterByDate(storage.getContributions(), config.startDate, config.endDate);
            result.finances = { expenses, contributions };
        }
        if (config.dataTypes.includes('gc')) {
            result.gc = this.filterByDate(storage.getGroupConscienceLog(), config.startDate, config.endDate);
        }
        if (config.dataTypes.includes('service')) {
            result.service = storage.getServicePositions();
        }
        if (config.dataTypes.includes('literature')) {
            result.literature = storage.getLiteratureInventory();
        }

        return result;
    },

    filterByDate(items, startDate, endDate) {
        if (!startDate && !endDate) return items;

        return items.filter(item => {
            const itemDate = new Date(item.date);
            if (startDate && itemDate < new Date(startDate)) return false;
            if (endDate && itemDate > new Date(endDate)) return false;
            return true;
        });
    },

    formatReport(data, config) {
        let html = `<div class="box">
            <h2>${sanitizeInput(config.name)}</h2>
            <p style="opacity: 0.8;">Generated: ${new Date().toLocaleDateString()}</p>`;

        if (config.startDate || config.endDate) {
            html += `<p>Date Range: ${config.startDate || 'Beginning'} to ${config.endDate || 'Present'}</p>`;
        }

        html += `<hr style="margin: 1rem 0;" />`;

        // Format each data type
        Object.keys(data).forEach(dataType => {
            html += this.formatSection(dataType, data[dataType]);
        });

        html += `</div>`;
        return html;
    },

    formatSection(type, data) {
        let html = `<h3>${type.charAt(0).toUpperCase() + type.slice(1)}</h3>`;

        switch (type) {
            case 'members':
                html += `<p>Total Members: ${data.length}</p>`;
                html += `<p>Home Group Members: ${data.filter(m => m.homegroup === 'Yes').length}</p>`;
                break;
            case 'attendance':
                const total = data.reduce((sum, a) => sum + a.count, 0);
                const avg = data.length > 0 ? (total / data.length).toFixed(1) : 0;
                html += `<p>Total Meetings: ${data.length}</p>`;
                html += `<p>Average Attendance: ${avg}</p>`;
                break;
            case 'finances':
                const totalExpenses = data.expenses.reduce((sum, e) => sum + parseFloat(e.amount), 0);
                const totalContributions = data.contributions.reduce((sum, c) => sum + parseFloat(c.amount), 0);
                html += `<p>Total Contributions: $${totalContributions.toFixed(2)}</p>`;
                html += `<p>Total Expenses: $${totalExpenses.toFixed(2)}</p>`;
                html += `<p>Net: $${(totalContributions - totalExpenses).toFixed(2)}</p>`;
                break;
            case 'gc':
                html += `<p>Total GC Items: ${data.length}</p>`;
                html += `<p>Approved: ${data.filter(gc => gc.status === 'approved').length}</p>`;
                html += `<p>Rejected: ${data.filter(gc => gc.status === 'rejected').length}</p>`;
                break;
            case 'service':
                const filled = data.filter(p => p.member).length;
                html += `<p>Total Positions: ${data.length}</p>`;
                html += `<p>Filled: ${filled}</p>`;
                html += `<p>Vacant: ${data.length - filled}</p>`;
                break;
            case 'literature':
                const totalItems = data.reduce((sum, l) => sum + l.quantity, 0);
                html += `<p>Total Items in Stock: ${totalItems}</p>`;
                html += `<p>Titles: ${data.length}</p>`;
                break;
        }

        html += `<hr style="margin: 1rem 0;" />`;
        return html;
    },

    exportToPDF(config) {
        const data = this.gatherData(config);
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();

        doc.setFontSize(20);
        doc.text(config.name, 20, 20);

        doc.setFontSize(10);
        doc.text('Generated: ' + new Date().toLocaleString(), 20, 30);

        if (config.startDate || config.endDate) {
            doc.text(`Date Range: ${config.startDate || 'Beginning'} to ${config.endDate || 'Present'}`, 20, 37);
        }

        let yPos = 50;

        Object.keys(data).forEach(dataType => {
            if (yPos > 250) {
                doc.addPage();
                yPos = 20;
            }

            doc.setFontSize(14);
            doc.text(dataType.charAt(0).toUpperCase() + dataType.slice(1), 20, yPos);
            yPos += 10;

            doc.setFontSize(10);

            switch (dataType) {
                case 'members':
                    doc.text(`Total Members: ${data[dataType].length}`, 25, yPos);
                    yPos += 7;
                    doc.text(`Home Group Members: ${data[dataType].filter(m => m.homegroup === 'Yes').length}`, 25, yPos);
                    yPos += 10;
                    break;
                case 'attendance':
                    const total = data[dataType].reduce((sum, a) => sum + a.count, 0);
                    const avg = data[dataType].length > 0 ? (total / data[dataType].length).toFixed(1) : 0;
                    doc.text(`Total Meetings: ${data[dataType].length}`, 25, yPos);
                    yPos += 7;
                    doc.text(`Average Attendance: ${avg}`, 25, yPos);
                    yPos += 10;
                    break;
                // ... similar for other types
            }
        });

        doc.save(`${config.name}.pdf`);
    }
};

function generateCustomReport() {
    const config = {
        name: document.getElementById('report-name').value.trim() || 'Custom Report',
        dataTypes: [],
        startDate: document.getElementById('report-start-date').value,
        endDate: document.getElementById('report-end-date').value
    };

    document.querySelectorAll('[data-report-data]:checked').forEach(cb => {
        config.dataTypes.push(cb.getAttribute('data-report-data'));
    });

    if (config.dataTypes.length === 0) {
        showToast('Please select at least one data type', 'error');
        return;
    }

    LoadingManager.show('Generating PDF...');
    setTimeout(() => {
        CustomReportBuilder.exportToPDF(config);
        LoadingManager.hide();
        showToast('Report generated successfully', 'success');
    }, 500);
}

function previewCustomReport() {
    const config = {
        name: document.getElementById('report-name').value.trim() || 'Custom Report',
        dataTypes: [],
        startDate: document.getElementById('report-start-date').value,
        endDate: document.getElementById('report-end-date').value
    };

    document.querySelectorAll('[data-report-data]:checked').forEach(cb => {
        config.dataTypes.push(cb.getAttribute('data-report-data'));
    });

    if (config.dataTypes.length === 0) {
        showToast('Please select at least one data type', 'error');
        return;
    }

    const html = CustomReportBuilder.generate(config);
    document.getElementById('report-preview').innerHTML = html;
}
```

---

## NEXT STEPS

1. This specification contains the foundation for all 4 categories
2. Each category has 5-10 major features outlined
3. Implementation will be done incrementally
4. Test each feature before moving to the next

## FILES TO CREATE

1. `enhancements-category1-ui.js` - All UI/UX JavaScript
2. `enhancements-category2-data.js` - Data management functions
3. `enhancements-category3-analytics.js` - Analytics engine
4. `enhancements-category4-reporting.js` - Reporting framework

These will be integrated into the main index.html file.
