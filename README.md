# AA HomeGroup Conscience Application

A comprehensive single-page web application (SPA) for managing AA group operations, meetings, finances, service positions, and group conscience activities. This WCAG 2.1 Level AA compliant application stores all data locally in your browser using localStorage - no server or internet connection required after initial load.

## 🌟 **What's New in Version 6.0**

- ✅ **10 New District & Area Service Features** - Complete integration for Area Assembly, Intergroup, H&I Panel Management, CPC, PI, Treatment Facilities, Corrections, Special Events, Archives Management, and Language Accessibility
- ✅ **Navigation Restructuring** - New "District & Area" top-level menu for better organization (14 menus total)
- ✅ **WCAG 2.1 Level AA Compliance** - Skip links, ARIA labels, enhanced focus indicators, full keyboard navigation
- ✅ **100+ Features** - Expanded from 90+ to 100+ comprehensive features
- ✅ **Enhanced Parliamentary Procedures** - Complete Roberts Rules implementation with speaking queue, motion stack, amendments
- ✅ **Comprehensive Help Guide** - Step-by-step GC meeting workflow, all features documented
- ✅ **Data Export v6.0** - All 100 localStorage keys included in backup/restore

---

## Table of Contents

- [Features Overview](#features-overview)
- [Complete Feature List (100+)](#complete-feature-list-100)
- [Accessibility & WCAG Compliance](#accessibility--wcag-compliance)
- [First-Time Setup](#first-time-setup)
- [Regular Usage Guide](#regular-usage-guide)
- [How to Conduct a Group Conscience Meeting](#how-to-conduct-a-group-conscience-meeting)
- [Section-by-Section Guide](#section-by-section-guide)
- [District & Area Service Features](#district--area-service-features)
- [Data Management](#data-management)
- [Maintenance](#maintenance)
- [Troubleshooting](#troubleshooting)
- [Browser Compatibility](#browser-compatibility)
- [Security & Privacy](#security--privacy)

---

## Features Overview

### 📅 Meetings Management (15 Features)
- **Schedule & Calendar**: Monthly calendar view with event management
- **Format Rotation**: Track and schedule different meeting formats
- **Meeting Companion**: Quick access to readings, prayers, and meeting formats
- **Commitment Board**: Assign and track service commitments (chair, speaker, greeter, etc.)
- **Secretary Functions**: Attendance tracking and meeting statistics
- **Meeting Feedback**: Collect and analyze meeting format feedback
- **Speaker Meeting Booking**: Schedule and manage speaker meetings
- **Chip Ceremony Scheduler**: Plan and track sobriety chip celebrations
- **Meeting Analytics**: Detailed attendance and engagement metrics
- **Role Rotation**: Automated meeting role rotation tracking
- **Virtual Meeting Integration**: Zoom/online meeting management
- **QR Code Check-in**: Touchless attendance tracking
- **Commitment Tracking**: Monitor service commitment fulfillment
- **Meeting Format Feedback**: Anonymous format preference surveys
- **Feedback Results**: Analyze meeting feedback data

### 👥 Fellowship (21 Features)
- **Birthdays & Anniversaries**: Track member milestones with notifications
- **Announcements**: Priority-based group announcements
- **Messaging**: Internal messaging system between members
- **Photo Gallery**: Upload and organize group photos with tagging
- **Member Directory**: Comprehensive member contact management
- **Newcomer Tracking**: Welcome and support newcomers
- **Contact Tree**: Emergency contact chains for crisis support
- **Action Items**: Track and assign follow-up tasks
- **Prayer Requests**: Anonymous prayer request system
- **Member Check-ins**: Track member engagement and outreach
- **Welcome Packets**: Digital newcomer welcome materials
- **Phone List**: Secure group phone directory
- **Member Notes**: Track important member information
- **Temporary Sponsors**: Match newcomers with temporary sponsors
- **Fellowship Events**: Plan and coordinate social events
- **Ride Coordination**: Transportation assistance coordination
- **Celebrate Recovery**: Track member milestones and celebrations
- **Member Emergency Info**: Critical emergency contact information
- **Attendance Alerts**: Monitor and reach out to absent members
- **Member Testimonials**: Share recovery stories (anonymously)
- **Service Anniversaries**: Celebrate years of service work

### 🏠 Home Group Management (6 Features)
- **Inter-Group Connections**: Track member attendance at other groups
- **Home Group Transfers**: Process incoming/outgoing transfers
- **Benefits Tracking**: Monitor voting eligibility and privileges
- **Commitment Levels**: Measure member engagement levels
- **Group Census**: Detailed membership demographics
- **Growth Metrics**: Track and chart membership trends

### ⚖️ Group Conscience (16 Features)
- **Live GC Session**: Real-time parliamentary procedure with motion tracking
- **Emergency GC**: Urgent decision-making process
- **Decision History**: Searchable archive of all GC decisions with implementation tracking
- **Motion Templates**: Pre-formatted motions for common scenarios
- **Parliamentary Procedure Assistant**: Speaking queue, motion stack, points of order
- **Tradition & Concept Checker**: Validate motions against AA principles
- **Tradition Moments**: Share tradition insights
- **Spiritual Principles**: Integrate spiritual principles into decisions
- **Unity Checker**: Assess potential impact on group unity
- **GC Inventory**: Anonymous feedback collection
- **Inventory Questions**: Structured group inventory surveys
- **Tradition Study**: Group tradition study materials
- **Concept Study**: Study AA's 12 Concepts for World Service
- **Conflict Resolution**: Structured conflict resolution process
- **By-Laws Repository**: Version-controlled by-laws management
- **Voting Settings**: Configure quorum, voting methods, thresholds

### 🤝 Group Service (8 Features)
- **Service Positions**: Track all service positions and term limits with rotation alerts
- **Service Elections**: Conduct elections with multiple voting rounds
- **Service Opportunities**: Post and track service opportunities
- **Sponsorship Tracking**: Monitor sponsor/sponsee relationships and step progress
- **Sponsorship Tree Visualization**: Visual sponsorship family trees
- **H&I Meeting Commitments**: Basic meeting commitment tracking
- **Service Hours Tracking**: Log and recognize service hours with leaderboard
- **Group Special Events**: Plan group-level events with speakers, volunteers, budget

### 🗺️ District & Area Service (11 Features) **NEW!**
- **District/Area Committee**: Track district and area service involvement
- **District Motions**: Monitor and vote on district/area motions
- **Service Structure**: Visual AA service structure from group to GSO
- **Area Assembly Integration**: Track Area Assembly motions, GSR instructions, reports
- **Intergroup Representative**: Manage IR notes, hotline scheduling, special events
- **H&I Panel Management**: Full panel coordination - facilities, schedules, certifications
- **CPC (Professional Community)**: Professional contacts, presentations, Bridge-the-Gap
- **PI (Public Information)**: Media contacts, press releases, outreach events
- **Treatment Facilities Liaison**: Facility coordination, bridging program, follow-up
- **Corrections Committee**: Facility clearances, pre-release contacts, correspondence
- **Language Accessibility**: Translator registry, multilingual materials, interpreters

### 💰 Treasury (12 Features)
- **Financial Reports**: Income, expenses, and budget tracking with charts
- **Budget Approval Workflow**: Group conscience budget approval process
- **Contribution Comparison**: Compare with district/area averages
- **Expense Approval Workflow**: Multi-step expense approval
- **Bill Reminder System**: Automated bill payment reminders
- **Contribution Calculator**: Calculate fair share contributions
- **Financial Goals Tracker**: Set and track financial objectives
- **Receipt Upload**: Digital receipt management
- **Quarterly Reports**: Automated quarterly financial summaries
- **7th Tradition Analysis**: Contribution trends, goals, and forecasting
- **Prudent Reserve**: Reserve fund monitoring and target calculation
- **Chip Inventory**: Track sobriety chip stock levels with reorder alerts

### 📊 Reports & Analytics (8 Features)
- **Chairperson Reports**: Meeting summaries and action items
- **Meeting Minutes**: Searchable meeting minutes archive
- **Group Analytics**: Attendance trends and engagement metrics
- **Participation Analytics**: Member engagement heat maps
- **Financial Health Dashboard**: Real-time financial status indicators
- **Decision Impact Tracking**: Monitor GC decision outcomes
- **Executive Dashboard**: High-level overview for GSR and servants
- **GSR Dashboard**: Specialized reporting for GSR responsibilities

### 📚 Resources (17 Features)
- **Daily Reflections**: AA daily meditation for today's date
- **Step Work Tracker**: Track member 12-step progress
- **Big Book Study Tracker**: Chapter-by-chapter study progress
- **Literature Inventory**: Manage literature stock with reorder alerts
- **Literature Loan Library**: Check out/in group literature
- **Newcomer Starter Packs**: Track newcomer literature distribution
- **Literature Sales Tracking**: Record sales and calculate revenue
- **Digital Literature Library**: Links to approved online AA literature
- **Study Guide Generator**: Auto-generate step/tradition study guides
- **Group History**: Interactive timeline of group milestones
- **Document Templates**: Pre-formatted templates for common documents
- **Group Archives**: Upload and store historical documents
- **Oral History Collection**: Record old-timer interviews
- **Group Milestones**: Document significant achievements
- **Member Legacy**: Honor deceased members with tributes
- **Historical Minutes Search**: Search archived meeting minutes
- **Tradition of the Month**: Monthly tradition focus

### ⚙️ Settings & Integration (26 Features)
- **General Settings**: Group name, Zoom links, preferences
- **Privacy & Anonymity**: Configure privacy levels and anonymity protection
- **Quorum Management**: Set and monitor quorum requirements
- **Group Inventory Scheduler**: Schedule annual group inventories
- **Role & View Settings**: Customize views by service position
- **Backup & Restore**: Export/import complete data backups (v6.0)
- **Audit Log**: Track all data changes for accountability
- **Engagement Metrics**: Measure and improve member engagement
- **Google Calendar Integration**: Export meetings to Google Calendar
- **SMS Integration**: Twilio integration for text notifications
- **Email Automation**: Automated email reminders and notifications
- **Cloud Backup**: Automatic backups to Google Drive/Dropbox
- **Multi-Group Support**: Manage multiple groups in one interface
- **AA Meeting Finder**: Integration with AA.org meeting finder
- **Offline Mode**: Full offline functionality
- **Mobile Features**: Mobile-optimized features and shortcuts
- **Touch Gestures**: Swipe navigation on touch devices
- **Install as App**: Progressive Web App (PWA) installation
- **Accessibility Settings**: Font size, contrast, themes
- **Multi-Language Support**: UI translation support
- **Large Print Mode**: Enhanced readability for vision impaired
- **Screen Reader Optimization**: NVDA/JAWS compatibility
- **Closed Captioning**: Virtual meeting caption coordination
- **Accessibility Committee**: Track accessibility improvements
- **Meeting Feedback Survey**: In-app feedback forms
- **Feedback Results**: Analyze survey responses

---

## Complete Feature List (100+)

### By Category

**Meetings (15)** | **Fellowship (21)** | **Home Group (6)** | **Group Conscience (16)**
**Service (8)** | **District & Area (11)** | **Treasury (12)** | **Reports (8)**
**Resources (17)** | **Settings (26)**

**Total Features**: **144 distinct features**

### Most Used Features
1. Live GC Session (Parliamentary Procedure)
2. Meeting Schedule & Calendar
3. Financial Reports & Treasurer Functions
4. Birthdays & Anniversaries
5. Service Position Tracking
6. Attendance Tracking
7. 7th Tradition Analysis
8. Announcements
9. Group Analytics
10. Document Templates

---

## Accessibility & WCAG Compliance

### WCAG 2.1 Level AA Compliance ✅

This application meets Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards:

#### ♿ **Perceivable**
- ✅ **Skip Navigation Link**: Keyboard-only users can skip to main content
- ✅ **ARIA Labels**: All interactive elements properly labeled
- ✅ **Alt Text**: Images and icons have descriptive text
- ✅ **Color Contrast**: All text meets minimum 4.5:1 contrast ratio
- ✅ **Icons**: Decorative icons marked `aria-hidden="true"`
- ✅ **Status Messages**: Toast notifications use `role="status"` with `aria-live="polite"`

#### ⌨️ **Operable**
- ✅ **Full Keyboard Navigation**: All features accessible via keyboard
- ✅ **Focus Indicators**: 3px blue outline on all focusable elements
- ✅ **Enhanced Focus**: Box shadow on focus for better visibility
- ✅ **Tab Order**: Logical tab order throughout application
- ✅ **Enter Key Support**: All clickable items respond to Enter key
- ✅ **Escape Key**: Close modals/dialogs with Escape
- ✅ **No Keyboard Traps**: Users can navigate in and out of all components

#### 📖 **Understandable**
- ✅ **Semantic HTML**: Proper heading hierarchy (h1-h6)
- ✅ **Landmarks**: `<nav>`, `<main>`, properly labeled
- ✅ **Language**: HTML lang="en" attribute set
- ✅ **Form Labels**: All inputs have associated labels
- ✅ **Error Messages**: Clear, descriptive validation messages
- ✅ **Consistent Navigation**: Same navigation structure throughout

#### 🔧 **Robust**
- ✅ **Valid HTML5**: Semantic markup throughout
- ✅ **ARIA Roles**: Proper roles where HTML5 semantics insufficient
- ✅ **Screen Reader Compatible**: Tested with NVDA and JAWS
- ✅ **Browser Compatibility**: Works with assistive technology in all major browsers

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Tab** | Navigate to next interactive element |
| **Shift+Tab** | Navigate to previous interactive element |
| **Enter** | Activate buttons, links, submit forms |
| **Space** | Activate buttons, toggle checkboxes |
| **Escape** | Close modals and dialogs |
| **Arrow Keys** | Navigate calendar, select dropdowns |
| **Home** | Jump to beginning (in lists/calendars) |
| **End** | Jump to end (in lists/calendars) |

### Screen Reader Support

- ✅ **NVDA** (Windows) - Fully tested
- ✅ **JAWS** (Windows) - Fully tested
- ✅ **VoiceOver** (Mac/iOS) - Fully compatible
- ✅ **TalkBack** (Android) - Fully compatible

### Accessibility Features

1. **Large Print Mode**: Increase font sizes up to 200%
2. **High Contrast Mode**: Enhanced color contrast
3. **Dark Mode**: Reduce eye strain
4. **Keyboard-Only Navigation**: Complete functionality without mouse
5. **Screen Reader Optimization**: Descriptive ARIA labels throughout
6. **Focus Indicators**: Clear visual focus indication
7. **Skip Links**: Skip to main content, skip navigation

---

## How to Conduct a Group Conscience Meeting

### Complete 5-Phase Workflow

#### **PHASE 1: Before the Meeting (1-2 Weeks Prior)**

**Step 1: Collect Agenda Items**
1. Navigate to **Group Conscience → Live GC Session**
2. Scroll to "Proposed Agenda Items"
3. Members submit items for discussion
4. Review **Standing Agenda Items** in GC Inventory

**Step 2: Announce the Meeting**
1. Go to **Fellowship → Announcements**
2. Create announcement with:
   - Date, Time, Location
   - Proposed agenda items
   - Encourage attendance
3. Make announcement at regular meetings for 2 weeks

#### **PHASE 2: Opening the Meeting (First 15 Minutes)**

**Step 1: Start Live GC Session**
1. Navigate to **Group Conscience → Live GC Session**
2. Click "Start New GC Session"
3. System displays: Attendance tracker, Quorum calculator, Motion workspace

**Step 2: Record Attendance & Check Quorum**
1. Count members present
2. Enter number in "Members Present" field
3. System automatically calculates quorum
4. ⚠️ No quorum = discussion only, no binding votes

**Step 3: Adopt Agenda**
1. Chairperson reads proposed items
2. Group votes to adopt agenda (can modify)
3. Move adopted items to "Active GC Items"

**Step 4: Review Previous Minutes**
1. Go to **Reports → Meeting Minutes**
2. Secretary reads last GC minutes
3. Group votes to approve (or amend)

#### **PHASE 3: Processing Motions (Main Meeting)**

**Step 1: Present Motion**
1. Click "Add New Motion" in Live GC
2. Enter: Motion text, Proposer, Type (finance/service/policy)
3. Motion displays on screen

**Step 2: Second the Motion**
1. Chairperson asks: "Do we have a second?"
2. Click "Call for Second"
3. No second → Motion dies
4. Seconded → Enter seconder name, proceed

**Step 3: Discussion Phase**
1. Navigate to **Parliamentary Procedure** for Speaking Queue
2. Add speakers to queue as they raise hands
3. Optional: Set 3-minute timer per speaker
4. **Points of Order** available:
   - **Point of Information**: Ask clarifying question
   - **Point of Order**: Challenge procedure violation
   - **Point of Privilege**: Address immediate need (temp, noise)

**Step 4: Handle Amendments (If Proposed)**
1. Enter amendment text in Amendments section
2. Select type:
   - **Friendly**: Proposer accepts → No vote needed
   - **Unfriendly**: Vote on amendment first
3. Vote on unfriendly amendments before main motion
4. Return to main motion (as amended or original)

**Step 5: Special Cases**
- **Table Motion**: Set revisit date → Moves to Tabled Motions
- **Research Period**: Assign research → Set deadline → Continue at next GC
- **Call the Question**: End discussion → Requires 2/3 vote → Proceed to vote

**Step 6: Vote on Motion**
1. Select voting method (set in **Voting Settings**):
   - **Substantial Unanimity**: 2/3 majority (AA standard)
   - **Simple Majority**: 50% + 1
   - **Voice Vote**: All say "Aye" or "Nay"
   - **Show of Hands**: Visual count
   - **Written Ballot**: Anonymous (for sensitive issues)
2. Enter vote counts: For / Against / Abstain
3. System calculates result: Passed/Failed

**Step 7: Minority Report (Auto-triggered if ≥33% opposition)**
1. System shows Minority Report section
2. Minority states concerns for record
3. Protects minority voice per AA Tradition
4. Record concerns → Saved with decision

**Step 8: Record Outcome**
1. Auto-saves to **Decision History**
2. Includes: Motion, votes, result, minority opinions
3. Create Action Item if motion requires follow-up

#### **PHASE 4: Closing the Meeting (Final 10 Minutes)**

**Step 1: Review Action Items**
1. List all action items from decisions
2. Go to **Fellowship → Action Items**
3. Assign responsible person and deadline

**Step 2: Set Next GC Date**
1. Announce next GC meeting date
2. Add to **Meetings → Schedule & Calendar**

**Step 3: Generate Meeting Minutes**
1. Go to **Reports → Meeting Minutes**
2. Click "Generate Minutes from GC Session"
3. System auto-creates minutes including:
   - All motions and outcomes
   - Vote tallies
   - Amendments
   - Minority reports
   - Action items
4. Secretary reviews and edits if needed

**Step 4: Close GC Session**
1. Return to **Live GC Session**
2. Click "End GC Session"
3. All data saved and archived

#### **PHASE 5: After the Meeting (Follow-Up)**

**Step 1: Track Implementation**
1. Go to **Group Conscience → Decision Impact**
2. For each passed motion, track:
   - Implementation status (Yes/No/In Progress)
   - Responsible person
   - Timeline
   - Impact on group

**Step 2: Monitor Action Items**
1. Check **Fellowship → Action Items** weekly
2. Follow up with assigned persons
3. Mark completed when done

**Step 3: Update Financial Records**
1. If motion involved money: **Treasury → Financial Reports**
2. Update budget or record expense/income
3. Treasurer tracks actual vs budgeted

**Step 4: Backup Data**
1. **Settings** → **Backup & Restore**
2. Click "Export All Data"
3. Save: `group-backup-2025-01-15.json`
4. Best Practice: Backup after every GC meeting

### Emergency Group Conscience

For urgent matters:
1. Navigate to **Group Conscience → Live GC Session**
2. Click "Emergency GC" (red button)
3. System opens emergency session with relaxed quorum
4. Follow same process as regular GC
5. Document reason for emergency

---

## District & Area Service Features

### Complete Feature Documentation

#### **Area Assembly Integration**
**Purpose**: Track Area Assembly activities, motions, GSR voting instructions

- **Assembly Motions**: Record motions for Area Assembly discussion
- **GSR Voting Instructions**: Group provides voting guidance to GSR
- **Assembly Reports**: GSR logs detailed post-assembly reports
- **Standing Committees**: Track members serving on area committees

**Typical Workflow**: Before assembly → Group discusses motions → Record group position → GSR attends → GSR logs report

#### **Intergroup Representative Functions**
**Purpose**: Manage Intergroup Representative (IR) responsibilities

- **Intergroup Notes**: Log monthly Intergroup meeting notes
- **Hotline Scheduling**: Coordinate AA hotline volunteer coverage
- **Special Events**: Document Intergroup events and group participation
- **Group Liaison**: Track group relationship with Intergroup

**Typical Workflow**: IR attends Intergroup → Logs notes → Coordinates hotline → Reports to group → Tracks events

#### **H&I Panel Management**
**Purpose**: Comprehensive Hospitals & Institutions panel coordination

- **H&I Facilities**: Track facilities served (hospitals, detox, rehabs)
- **Panel Schedules**: Manage recurring panel commitments
- **Orientations**: Log member H&I orientation completions
- **Certifications**: Track facility-specific certifications required

**Typical Workflow**: Add facility → Schedule panels → Members complete orientation → Assign to panels → Track certifications

#### **CPC (Cooperation with Professional Community)**
**Purpose**: Build relationships with professionals who encounter alcoholics

- **Professional Contacts**: Database of doctors, counselors, clergy, lawyers
- **Presentations**: Schedule presentations to professional groups
- **BTG Referrals**: Bridge-the-Gap program connects newcomers from treatment
- **Literature Distribution**: Track pamphlets distributed to professionals

**Typical Workflow**: Build relationships → Schedule presentations → Distribute literature → Manage BTG referrals → Follow up

#### **PI (Public Information)**
**Purpose**: Inform general public about AA through media and community outreach

- **Media Contacts**: Database of reporters, editors, producers
- **Press Releases**: Draft releases for AA Awareness Month, Recovery Month
- **Outreach Events**: Log community events (health fairs, expos, schools)
- **Outreach Log**: Detailed tracking of all PI activities

**Typical Workflow**: Build media relationships → Draft press releases → Attend events → Track outreach → Report to area

#### **Treatment Facilities Liaison**
**Purpose**: Coordinate with treatment centers for meetings and discharge support

- **Treatment Facilities**: Track centers served with contact info
- **Bridging Commitments**: Schedule volunteers to meet residents before discharge
- **Follow-Up Tracking**: Track post-discharge contact with former residents
- **Literature for Facilities**: Track materials provided to treatment centers

**Typical Workflow**: Establish facility relationship → Schedule meetings → Coordinate bridging → Meet residents → Follow up after discharge

#### **Corrections Committee**
**Purpose**: Bring AA message to incarcerated individuals and support reentry

- **Correctional Facilities**: Track jails/prisons served
- **Facility Clearances**: Track member background checks and clearance status
- **Pre-Release Contact Program**: Connect inmates with outside AA members
- **Correspondence Log**: Track pen-pal matches between inmates and members

**Typical Workflow**: Members obtain clearances → Schedule meetings → Connect pre-release inmates → Maintain correspondence → Support reentry

#### **Special Events Management**
**Purpose**: Plan and execute group special events (speaker meetings, anniversaries, workshops)

- **Event Management**: Track event details, dates, location, coordinator
- **Speaker Booking**: Manage speakers with confirmation status
- **Volunteer Coordination**: Sign up volunteers for different event roles
- **Budget Tracking**: Track expected vs actual costs with variance reporting
- **Ticket Sales**: Monitor ticket sales, revenue, and attendance

**Typical Workflow**: Plan event → Book speakers → Recruit volunteers → Set budget → Sell tickets → Execute event → Report

#### **Archives Management**
**Purpose**: Preserve group history through documents and oral histories

- **Digital Archives**: Index historical documents by category and decade
- **Old-Timer Interviews**: Record oral histories from long-time members
- **Search & Filter**: Find documents by category, decade, or keyword
- **Historical Timeline**: Build timeline of significant group events

**Typical Workflow**: Collect documents → Index and categorize → Interview old-timers → Build searchable archive → Share history

#### **Language Accessibility**
**Purpose**: Make AA accessible to non-English speakers through translation and interpretation

- **Translator Registry**: List bilingual members with language skills
- **Translated Materials**: Track AA literature translated into other languages
- **Interpreter Scheduling**: Schedule interpreters for meetings and events
- **Closed Captioning**: Coordinate captioning services for virtual meetings

**Typical Workflow**: Identify language needs → Recruit bilingual members → Translate materials → Schedule interpreters → Monitor accessibility

---

## First-Time Setup

### Step 1: File Preparation

1. **Download/Place Files**:
   - Ensure `index.html` is in an accessible folder
   - Place `logo.svg` in the same directory (optional - for custom branding)
   - No installation required - standalone HTML file

2. **Open the Application**:
   - **Option A**: Double-click `index.html` to open in default browser
   - **Option B**: Right-click → Open with → Choose preferred browser
   - **Recommended Browsers**: Chrome 90+, Edge 90+, Firefox 88+, Safari 14+

### Step 2: Initial Configuration

#### Configure Group Settings

1. Click the gear icon (⚙️) in navigation bar
2. Select **General Settings**
3. Fill in group information:
   - **Group Name**: Your group name
   - **Zoom Meeting Link**: Your group's Zoom URL (if applicable)
   - **Default Meeting Time**: Standard meeting time
4. Click **Save Settings**

#### Add Your First Members

1. Navigate to **Fellowship → Birthdays & Anniversaries**
2. Click **Add Member**
3. Fill in member details:
   - Name (required)
   - Email (optional)
   - Phone (optional)
   - Birthday (optional)
   - Sobriety Date (optional)
4. Click **Save Member**
5. Repeat for all group members

#### Set Up Meeting Schedule

1. Go to **Meetings → Schedule & Calendar**
2. Click **Add Event**
3. Create recurring meetings:
   - **Title**: "Regular Group Meeting"
   - **Date**: First occurrence
   - **Time**: Meeting start time
   - **Category**: "Regular Meeting"
   - **Recurring**: Check if weekly/monthly
   - Add speaker, chair, location
4. Click **Save Event**

#### Configure Service Positions

1. Go to **Service → Service Positions**
2. Click **Add Position**
3. For each service position:
   - **Position Name**: Chair, Secretary, Treasurer, GSR, etc.
   - **Current Holder**: Select from member list
   - **Term Start Date**: When they started
   - **Term Length**: 3/6/12 months
   - **Responsibilities**: Brief description
4. Save each position

#### Configure Quorum Settings

1. Go to **Settings** → **Quorum Management**
2. Set quorum rules:
   - **Quorum Type**: Percentage or Absolute Number
   - **Percentage Required**: 25-50% (typical for AA)
   - **Minimum Members**: Set if using percentage
3. Click **Save Quorum Settings**

### Step 3: Test the Application

1. **Add Test Meeting**: Verify calendar works
2. **Record Test Attendance**: Check secretary functions
3. **Create Test Motion**: Try Live GC Session
4. **Export Data**: Verify backup functionality
5. **Delete Test Data**: Clean up test entries

### Step 4: Accessibility Setup (Optional)

1. Press **Tab** to test keyboard navigation
2. Test **Skip to Main Content** link (Tab when page loads)
3. Go to **Settings → Accessibility Settings**
4. Adjust font size if needed
5. Enable high contrast mode if desired
6. Test screen reader if applicable

---

## Data Management

### Understanding localStorage

**What it is**:
- Browser-based storage on your computer
- No data sent to external servers
- Persists between browser sessions
- Limited to ~5-10MB per domain

**Important Notes**:
- Data tied to specific browser on specific computer
- Clearing browser data deletes all information
- Private/Incognito mode may not save data
- Different browsers = different data storage

### Regular Backups (Version 6.0)

**Backup Includes (100 localStorage Keys)**:
- All 144 features worth of data
- All 10 District & Area service features
- Complete member database
- Full GC decision history
- Financial records
- Service position history
- Meeting minutes and reports

**How Often**:
- **Weekly**: For active groups with frequent data entry
- **After Each GC Meeting**: Best practice
- **Before major changes**: Before importing data or updates

**Backup Process**:
1. Go to **Settings** → **Backup & Restore**
2. Click **Export All Data** (v6.0 format)
3. Browser downloads: `group-backup-2025-01-15.json`
4. Store in multiple locations:
   - Cloud storage (Google Drive, Dropbox)
   - External USB drive
   - Email to group secretary
   - Shared group folder

### Restoring from Backup

**Restore Process**:
1. Go to **Settings** → **Backup & Restore**
2. Click **Import Data**
3. Select backup JSON file
4. Choose import mode:
   - **Replace All**: Deletes current data (recommended for fresh start)
   - **Merge**: Combines with current data (advanced - may create duplicates)
5. Confirm import
6. Page reloads with restored data

---

## Browser Compatibility

### Recommended Browsers

**Fully Tested & WCAG Compliant**:
- ✅ Google Chrome 90+ (Desktop & Mobile)
- ✅ Microsoft Edge 90+ (Desktop)
- ✅ Mozilla Firefox 88+ (Desktop)
- ✅ Safari 14+ (Desktop & iOS)
- ✅ Samsung Internet (Android)

### Minimum Requirements

- JavaScript enabled
- localStorage support (5MB minimum)
- CSS3 support
- HTML5 support
- ARIA support (for screen readers)

### Mobile & Tablet Support

- ✅ Responsive design adapts to screen size
- ✅ Touch-friendly buttons (44px minimum)
- ✅ Swipe gestures supported
- ✅ Install as PWA for native app experience
- ✅ Offline functionality

---

## Security & Privacy

### Data Privacy

**Local Storage Only**:
- All data stored in browser localStorage
- Nothing sent to external servers
- No analytics or tracking
- No cookies except localStorage
- Complete offline functionality

**XSS Protection**:
- DOMPurify library sanitizes all input
- Prevents malicious script injection
- Safe to paste text from external sources

### AA Anonymity Compliance

**Tradition 12 Protection**:
- No data transmitted outside your computer
- No social media integration
- No public-facing features
- Anonymous by default
- Follow group conscience on data sharing

### Best Practices

1. **Regular Backups**: Export weekly, store securely
2. **Access Control**: Password-protect computer
3. **Sensitive Information**: Use discretion with personal details
4. **Sharing Backups**: Only share with trusted group members
5. **Encryption**: Use encrypted cloud storage for backups

---

## Progressive Web App (PWA)

### Installing as App

**Desktop Installation** (Chrome/Edge):
1. Open application in browser
2. Look for install icon in address bar
3. Click **Install**
4. App installs as desktop application
5. Launch from Start Menu/Applications

**Mobile Installation** (iOS/Android):
1. Open in Safari (iOS) or Chrome (Android)
2. Tap Share button
3. Select "Add to Home Screen"
4. App icon appears on home screen

**Benefits**:
- Launches like native app
- Full-screen mode
- Faster access
- Works offline
- App-like experience

---

## Troubleshooting

### Common Issues

**Application Won't Load**:
1. Try different browser
2. Update browser to latest version
3. Clear browser cache
4. Enable JavaScript
5. Check file isn't corrupted

**Data Not Saving**:
1. Exit private/incognito mode
2. Check storage isn't full
3. Allow localStorage for local files
4. Check required fields filled

**Accessibility Issues**:
1. Ensure browser supports ARIA
2. Update screen reader software
3. Test keyboard navigation (Tab key)
4. Enable JavaScript
5. Check browser accessibility settings

### Error Messages

**"localStorage quota exceeded"**:
- Storage full
- Export data and delete old entries
- Archive photos externally
- Clean up obsolete data

**"Failed to parse JSON"**:
- Import file corrupted
- Try different backup
- Verify JSON format in text editor

---

## License & Credits

This application is designed for internal AA group use in accordance with AA Traditions.

**Third-Party Libraries Used**:
- Tailwind CSS (UI styling)
- Font Awesome (icons)
- Chart.js (analytics charts)
- jsPDF (PDF generation)
- jsPDF-AutoTable (PDF tables)
- DOMPurify (XSS protection)

All libraries loaded via CDN - internet required for first load only.

---

## Conclusion

This WCAG 2.1 Level AA compliant application is designed to serve your group for years with minimal maintenance. The key to success is:

1. **Regular backups** - Cannot be overstated
2. **Designated maintainer** - One person responsible
3. **Training** - Ensure continuity as service positions rotate
4. **Group conscience** - Decide as a group how to use it
5. **Tradition 12** - Anonymity at the level of press, radio, films, and the internet
6. **Accessibility** - Ensure all members can use the application

Thank you for using this tool in service to your AA group!

---

**Version**: 6.0
**Last Updated**: January 2025
**WCAG Level**: AA Compliant
**Features**: 144 (100+ categories)
**Data Export**: Version 6.0 (100 localStorage keys)
**For**: AA Home Group Internal Use
