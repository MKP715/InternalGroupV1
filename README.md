# Rowlett Group - AA Group Conscience Application

A comprehensive single-page web application (SPA) for managing AA group operations, meetings, finances, service positions, and group conscience activities. This application stores all data locally in your browser using localStorage - no server or internet connection required after initial load.

## Table of Contents

- [Features Overview](#features-overview)
- [First-Time Setup](#first-time-setup)
- [Regular Usage Guide](#regular-usage-guide)
- [Section-by-Section Guide](#section-by-section-guide)
- [Data Management](#data-management)
- [Maintenance](#maintenance)
- [Troubleshooting](#troubleshooting)
- [Browser Compatibility](#browser-compatibility)
- [Security & Privacy](#security--privacy)

---

## Features Overview

### Meetings Management
- **Schedule & Calendar**: Monthly calendar view with event management
- **Format Rotation**: Track and schedule different meeting formats
- **Meeting Companion**: Quick access to readings, prayers, and meeting formats
- **Commitment Board**: Assign and track service commitments (chair, speaker, greeter, etc.)
- **Secretary Functions**: Attendance tracking and meeting statistics

### Fellowship
- **Birthdays & Anniversaries**: Track member milestones
- **Announcements**: Post and manage group announcements with priority levels
- **Messaging**: Internal messaging system between members
- **Photo Gallery**: Upload and organize group photos with tagging

### Group Conscience
- **Live GC Session**: Real-time agenda queue during group conscience meetings
- **Decision History**: Searchable archive of all GC decisions
- **GC Inventory**: Anonymous feedback collection
- **Guidelines & By-Laws**: Version-controlled document management

### Service
- **Service Positions**: Track all service positions and term limits
- **Sponsorship Tracking**: Monitor sponsor/sponsee relationships
- **District/Area Committee**: GSR reports and district meeting schedules

### Treasury
- **Financial Reports**: Income, expenses, and budget tracking
- **7th Tradition Analysis**: Contribution trends and goals
- **Prudent Reserve**: Reserve fund monitoring
- **Chip Inventory**: Track sobriety chip stock levels

### Reports & Analytics
- **Chairperson Reports**: Meeting summaries and action items
- **Group Analytics**: Attendance trends and engagement metrics

### Resources
- **AA Literature Library**: Track group library and checkouts
- **Group History**: Interactive timeline of group milestones
- **Document Templates**: Pre-formatted templates for common documents

### Settings
- **General Settings**: Group name, Zoom links, and preferences
- **Accessibility**: Font size, contrast, and screen reader support

---

## First-Time Setup

### Step 1: File Preparation

1. **Download/Place Files**:
   - Ensure `index.html` is in an accessible folder
   - Place `logo.svg` in the same directory (for branding)
   - No installation required - this is a standalone HTML file

2. **Open the Application**:
   - **Option A**: Double-click `index.html` to open in your default browser
   - **Option B**: Right-click → Open with → Choose your preferred browser
   - **Recommended Browsers**: Chrome, Edge, Firefox, Safari (latest versions)

### Step 2: Initial Configuration

#### Configure Group Settings

1. Click the gear icon (⚙️) in the navigation bar
2. Select **General Settings**
3. Fill in your group information:
   - **Group Name**: "Rowlett Group" (or your group name)
   - **Zoom Meeting Link**: Your group's Zoom URL (if applicable)
   - **Default Meeting Time**: Standard meeting time
   - Click **Save Settings**

#### Add Your First Members

1. Navigate to **Home** (if not already there)
2. Scroll down to find member management (or go to Settings → Member Management)
3. Click **Add New Member**
4. Fill in member details:
   - Name (required)
   - Email (optional)
   - Phone (optional)
   - Birthday (optional - for birthday tracking)
   - Sobriety Date (optional)
5. Click **Save Member**
6. Repeat for all group members

#### Set Up Meeting Schedule

1. Go to **Meetings** → **Schedule & Calendar**
2. Click **Add Event**
3. Create your recurring meetings:
   - **Title**: "Regular Group Meeting"
   - **Date**: Select the first occurrence
   - **Time**: Meeting start time
   - **Category**: "Regular Meeting"
   - **Recurring**: Check if weekly/monthly
   - Optional: Add speaker, chair, location
4. Click **Save Event**

#### Configure Meeting Formats

1. Go to **Meetings** → **Format Rotation**
2. Click **Add Format**
3. Set up your rotation:
   - **Week**: Week 1, 2, 3, 4, etc.
   - **Format Type**: Speaker, Discussion, Step Study, etc.
   - **Description**: Format details
   - **Reading Assignments**: Specific pages/chapters
4. Save and repeat for your full rotation cycle

#### Set Up Service Positions

1. Go to **Service** → **Service Positions**
2. Click **Add Position**
3. For each service position:
   - **Position Name**: Chair, Secretary, Treasurer, GSR, etc.
   - **Current Holder**: Select from member list
   - **Term Start Date**: When they started
   - **Term Length**: 3 months, 6 months, 1 year, etc.
   - **Responsibilities**: Brief description
4. Save each position

#### Configure Financial Settings (Treasurer)

1. Go to **Treasury** → **Prudent Reserve**
2. Set your reserve target:
   - **Monthly Expenses**: Average monthly rent + literature + supplies
   - **Reserve Months**: 3-6 months (as per group conscience)
   - Click **Calculate & Save**

3. Go to **Treasury** → **Financial Reports**
4. Set up budget categories:
   - Rent
   - Literature
   - Supplies
   - Contributions to District/Area
   - Website/Technology
   - Prudent Reserve

5. Go to **Treasury** → **Chip Inventory**
6. Enter current chip stock levels for each type

### Step 3: Enable Browser Notifications (Optional)

1. When prompted, click **Allow** to enable desktop notifications
2. Notifications will alert you for:
   - Upcoming meetings (24 hours in advance)
   - Birthdays (7 days in advance)
   - Service commitments (2 days in advance)

### Step 4: Bookmark for Easy Access

1. Press `Ctrl+D` (Windows) or `Cmd+D` (Mac)
2. Save bookmark as "Rowlett Group - Home"
3. Add to bookmarks bar for quick access

---

## Regular Usage Guide

### Daily/Weekly Tasks

#### Before Each Meeting

1. **Check Schedule**:
   - Go to **Meetings** → **Schedule & Calendar**
   - Review today's events and upcoming meetings

2. **Review Format**:
   - Go to **Meetings** → **Format Rotation**
   - Check current week's format
   - Note any special readings or topics

3. **Check Commitments**:
   - Go to **Meetings** → **Commitment Board**
   - Verify who is chairing, speaking, greeting, etc.
   - Follow up with members if needed

4. **Prepare Readings**:
   - Go to **Meetings** → **Meeting Companion**
   - Access required readings for the format
   - Print or display on screen if needed

#### During the Meeting

1. **Track Attendance** (Secretary):
   - Go to **Meetings** → **Secretary Functions**
   - Click **Record Attendance**
   - Select date and mark attendees
   - Note newcomers if applicable

2. **Live Group Conscience** (if scheduled):
   - Go to **Group Conscience** → **Live GC Session**
   - Add agenda items as they come up
   - Mark items as discussed
   - Track motions and votes

#### After Each Meeting

1. **Log 7th Tradition** (Treasurer):
   - Go to **Treasury** → **7th Tradition Analysis**
   - Enter date and contribution amount
   - Application tracks trends automatically

2. **Record Chip Distributions** (if applicable):
   - Go to **Treasury** → **Chip Inventory**
   - Log each chip given out
   - Inventory updates automatically

3. **Post Announcements**:
   - Go to **Fellowship** → **Announcements**
   - Add any announcements made
   - Set priority (Urgent, Normal, Info)

4. **Update Action Items**:
   - Go to **Group Conscience** → **Live GC Session** or **Decision History**
   - Track follow-up items
   - Update status as completed

### Monthly Tasks

#### Service Position Rotation

1. **Check Term Expiration**:
   - Go to **Service** → **Service Positions**
   - Review positions with expiring terms (highlighted)
   - Plan for elections if needed

2. **Open Nominations**:
   - Go to **Service** → **Service Positions**
   - Click **Add Nomination** for open positions
   - Record interested members

#### Financial Reports

1. **Generate Monthly Report**:
   - Go to **Treasury** → **Financial Reports**
   - Review income vs. expenses
   - Check prudent reserve status
   - Export as PDF for group records

2. **Update Budget**:
   - Add any new expense categories
   - Adjust budgets based on actual spending

#### Group Conscience Preparation

1. **Review Pending Items**:
   - Go to **Group Conscience** → **Decision History**
   - Check unresolved items
   - Prepare agenda

2. **Collect Anonymous Feedback**:
   - Go to **Group Conscience** → **GC Inventory**
   - Review any submitted feedback
   - Add to GC agenda if needed

### Quarterly Tasks

#### Analytics Review

1. **Generate Reports**:
   - Go to **Reports** → **Group Analytics**
   - Select time range (30/90/180 days)
   - Review attendance trends
   - Check engagement metrics

2. **Export Data for Archives**:
   - Go to **Settings** → **General Settings**
   - Click **Export All Data**
   - Save JSON file with date in filename
   - Store in secure location

#### By-Laws Review

1. **Check for Amendments**:
   - Go to **Group Conscience** → **Guidelines & By-Laws**
   - Review amendment history
   - Update current by-laws if needed

---

## Section-by-Section Guide

### Home Dashboard

**Purpose**: At-a-glance view of group status

**What you'll see**:
- Next 5 upcoming meetings
- Today's birthdays and upcoming this month
- Recent announcements
- Recent photos
- Quick stats (total members, active positions, etc.)

**Actions**:
- Click any section to jump to detailed view
- Use Zoom meeting button (if configured) to launch meetings

### Meetings → Schedule & Calendar

**Adding an Event**:
1. Click **Add Event**
2. Fill in all required fields (marked with *)
3. For recurring meetings, check **Recurring** and set pattern
4. Assign speaker/chair if known
5. Click **Save Event**

**Editing an Event**:
1. Find event in calendar or list
2. Click **Edit** button
3. Make changes
4. Click **Update Event**

**Deleting an Event**:
1. Find event
2. Click **Delete**
3. Confirm deletion

**Calendar Navigation**:
- Use **Previous/Next Month** arrows
- Click on any date to see events
- Events show as colored chips in calendar cells

### Meetings → Format Rotation

**Setting Up Weekly Rotation**:
1. Click **Add Format**
2. Assign week number (1-4 or 1-5 for months with 5 weeks)
3. Select format type from dropdown
4. Add description and readings
5. Save

**Viewing Current Format**:
- Current week's format shows at top
- Highlights in different color
- Lists all readings and special instructions

### Meetings → Meeting Companion

**Purpose**: Quick access to readings during meetings

**Available Readings**:
- How It Works (Big Book, Chapter 5)
- The Twelve Steps
- The Twelve Traditions
- The Twelve Concepts
- Promises (9th Step, 10th Step, 12th Step)
- Group formats (Speaker, Discussion, Step Study, etc.)

**Using During Meeting**:
1. Navigate to Meeting Companion
2. Click the reading needed
3. Content displays with proper formatting
4. Read directly from screen or print

### Meetings → Commitment Board

**Assigning Commitments**:
1. Click **Add Commitment**
2. Select:
   - Date of commitment
   - Role (Chair, Speaker, Greeter, Literature, etc.)
   - Member assigned
   - Whether to send reminder (2 days ahead)
3. Save

**Viewing Commitments**:
- **Current Week**: Shows this week's assignments
- **Full Calendar**: Shows all upcoming commitments
- **Gaps**: Highlights unfilled roles in red

**Reminder Notifications**:
- If enabled, browser notification 2 days before
- Also shows in-app notification

### Meetings → Secretary Functions

**Recording Attendance**:
1. Click **Record Attendance**
2. Select meeting date
3. Check boxes for all attendees
4. Note newcomer count (optional)
5. Save

**Viewing Statistics**:
- Average attendance
- Attendance trends graph
- Most frequent attendees
- Newcomer tracking

**Exporting Attendance Data**:
- Click **Export to PDF**
- Generates formatted report
- Include date range in filename

### Fellowship → Birthdays & Anniversaries

**Adding Birthday/Anniversary**:
1. Select member from dropdown (or add new member)
2. Enter birthday date
3. Enter sobriety date (for anniversary)
4. Save

**Viewing**:
- **This Month**: All birthdays/anniversaries this month
- **Upcoming**: Next 30 days
- **All**: Complete list sorted by month

**Notifications**:
- In-app notification on actual day
- Browser notification 7 days ahead (if enabled)

### Fellowship → Announcements

**Creating Announcement**:
1. Click **Add Announcement**
2. Enter title and message
3. Set priority:
   - **Urgent**: Red border, shows first
   - **Normal**: Blue border
   - **Info**: Gray border
4. Save

**Reading Announcements**:
- Unread announcements highlighted
- Click **Mark as Read** to dismiss
- Recent announcements show on Home dashboard

### Fellowship → Messaging

**Sending a Message**:
1. Click **Compose New Message**
2. Select recipient(s) from member list
3. Enter subject
4. Write message
5. Click **Send**

**Reading Messages**:
- **Inbox**: Received messages
- **Sent**: Messages you've sent
- **Drafts**: Saved but not sent
- Unread count shows on navigation badge

**Note**: Messages stored locally, not actually transmitted

### Fellowship → Photo Gallery

**Uploading Photos**:
1. Click **Upload Photo**
2. Select image file from computer
3. Add caption (optional)
4. Add tags (comma-separated): "fellowship", "anniversary", "event", etc.
5. Upload

**Viewing Photos**:
- Grid view shows all photos
- Click photo for full-screen modal
- Use arrows or keyboard to navigate
- Press ESC to close modal

**Filtering by Tags**:
1. Enter tag in filter box
2. Click **Filter**
3. Shows only photos with that tag

**Organizing**:
- Add/edit tags after upload
- Delete unwanted photos
- Caption photos for context

### Group Conscience → Live GC Session

**During Group Conscience Meeting**:
1. Open **Live GC Session**
2. Click **Add Item** as topics arise
3. Items appear in queue
4. Click **Mark Discussed** when addressed
5. Items remain in history

**Making Motions**:
1. In Live GC or Decision History section
2. Click **Add Motion**
3. Record:
   - Motion text
   - Who made motion
   - Who seconded
   - Discussion summary
   - Vote results (For/Against/Abstain)
   - Decision (Passed/Failed)
4. Save - adds to permanent Decision History

### Group Conscience → Decision History

**Viewing Past Decisions**:
- **All Decisions**: Complete history
- **Filter by Year**: Select year from dropdown
- **Filter by Status**: Passed, Failed, Tabled
- **Search**: Enter keywords to find specific decisions

**Linking Related Motions**:
- When viewing a decision, click **Link Related Motion**
- Creates cross-references between related decisions
- Useful for tracking amendments to previous decisions

**Exporting**:
- Click **Export to PDF**
- Generates formatted report of all decisions
- Include date range for partial export

### Group Conscience → GC Inventory

**Anonymous Feedback Collection**:
1. Click **Submit Anonymous Feedback**
2. Enter feedback (no name required)
3. Submit

**Reviewing Feedback** (Secretary/Chair):
- View all submitted feedback
- Use during group conscience to address concerns
- Delete after addressed

**Purpose**:
- Allows members to voice concerns anonymously
- Helps identify issues needing group conscience

### Group Conscience → Guidelines & By-Laws

**Uploading Current By-Laws**:
1. Click **Upload New Version**
2. Paste or type current by-laws
3. Add version number (1.0, 2.0, etc.)
4. Add change summary if amendment
5. Save

**Tracking Amendments**:
- Each version stored with date
- Shows what changed between versions
- Links to GC decisions that prompted changes

**Viewing**:
- **Current**: Active by-laws
- **History**: All past versions
- **Compare**: Side-by-side version comparison

### Service → Service Positions

**Managing Positions**:
1. **Add Position**: New service role
2. **Edit Position**: Update holder or details
3. **Term Expiration Warnings**:
   - Yellow badge: 30 days remaining
   - Red badge: Term expired

**Election Management**:
1. When term expiring, click **Open Nominations**
2. Members can nominate themselves or others
3. During election, record winner
4. Updates position holder and resets term

**Reports**:
- **All Positions**: Current holders and terms
- **Expiring Soon**: Positions needing rotation
- **Position History**: Who held position when

### Service → Sponsorship Tracking

**Recording Sponsorship**:
1. Click **Add Sponsorship**
2. Select:
   - Sponsor name
   - Sponsee name
   - Type: Temporary or Program
   - If Program, enter current step
3. Save

**Updating Progress**:
- Click **Update** next to sponsorship
- Change step number
- Add notes about progress

**Viewing Sponsorship Tree**:
- Visual tree showing sponsor chains
- Helps identify "family trees" in recovery
- Shows active vs. completed sponsorships

### District/Area Committee

**GSR Reports**:
1. After district meeting, click **Add GSR Report**
2. Enter:
   - Meeting date
   - Meeting type (District, Area, etc.)
   - Report summary
   - Action items for group
3. Save

**District Meeting Schedule**:
- Add upcoming district meetings
- Set location and time
- Reminder notifications

**DCM Communications**:
- Log communications from DCM
- Share with group as needed

### Treasury → Financial Reports

**Logging Income**:
1. Click **Add Income**
2. Enter:
   - Date
   - Source: 7th Tradition, Literature Sales, Other
   - Amount
   - Description
3. Save

**Logging Expenses**:
1. Click **Add Expense**
2. Enter:
   - Date
   - Category: Rent, Literature, Supplies, etc.
   - Amount
   - Description/Receipt info
3. Save

**Viewing Reports**:
- **Monthly Summary**: Current month income/expenses
- **Year-to-Date**: Annual totals
- **Budget vs. Actual**: Compare to budget
- **Charts**: Visual spending breakdown

**Exporting**:
- Click **Export to PDF**
- Professional financial report
- Include charts and tables

### Treasury → 7th Tradition Analysis

**Weekly Contribution Tracking**:
1. After each meeting, add contribution amount
2. Application tracks:
   - Weekly average
   - Monthly totals
   - Year-over-year comparison
   - Trends

**Setting Goals**:
- Enter target weekly/monthly contribution
- Dashboard shows progress toward goal
- Alerts if falling short

**Viewing Trends**:
- Line chart shows contribution patterns
- Identifies seasonal variations
- Helps with budget planning

### Treasury → Prudent Reserve

**Setting Target**:
1. Enter monthly expenses
2. Choose reserve months (3-6 typical)
3. Click **Calculate**
4. Save target

**Monitoring**:
- Dashboard shows current reserve amount
- Progress bar toward target
- Alert if below target

**Adjusting**:
- Update target as expenses change
- Review quarterly

### Treasury → Chip Inventory

**Updating Inventory**:
1. Select chip type
2. Enter current quantity
3. Set low stock threshold
4. Save

**Alerts**:
- Red alert when below threshold
- Reminds treasurer to order

**Distribution Logging**:
1. When giving chip, click **Log Distribution**
2. Select chip type
3. Enter recipient name (or "Anonymous")
4. Save
5. Inventory decrements automatically

**Reordering**:
- View low stock alerts
- Generate order list
- Update inventory when chips arrive

### Reports → Chairperson Reports

**Creating Report**:
1. After meeting, click **Add Report**
2. Enter:
   - Meeting date
   - Attendance count
   - Topics discussed
   - Decisions made
   - Action items
3. Save

**Viewing History**:
- All past reports chronologically
- Search by date or keyword
- Export as PDF

**Purpose**:
- Official meeting minutes
- Track action items
- Historical record

### Reports → Group Analytics

**Available Metrics**:
1. **Attendance Trends**: Line chart over time
2. **Engagement Metrics**: Active members percentage
3. **GC Participation**: Voting rates, discussion activity
4. **Service Engagement**: Filled positions, commitment rates
5. **Activity Summary**: Overall group health

**Time Ranges**:
- Last 30 days
- Last 90 days
- Last 180 days
- Last year
- All time

**Using Analytics**:
- Identify attendance patterns
- Plan for low-attendance periods
- Recognize highly engaged members
- Find areas needing attention

### Resources → AA Literature Library

**Adding Books/Literature**:
1. Click **Add Item**
2. Enter:
   - Title
   - Author (if applicable)
   - Type: Book, Pamphlet, Grapevine, etc.
   - Quantity owned
   - Purchase date
3. Save

**Checking Out Literature**:
1. Find item in catalog
2. Click **Check Out**
3. Select member
4. Set due date (optional)
5. Save

**Checking In**:
1. View **Current Checkouts**
2. Find item
3. Click **Mark Returned**

**Inventory**:
- Shows all items
- Availability status
- Overdue items highlighted

### Resources → Group History

**Adding Historical Events**:
1. Choose timeline: AA Genesis, DFW Area, or Rowlett Group
2. Click **Add Event**
3. Enter:
   - Date
   - Title
   - Description
   - Additional details (for hover popup)
4. Save

**Viewing**:
- Interactive timeline with alternating left/right layout
- Hover over events for detailed popup
- Click events for full information
- Educational for newcomers

### Resources → Document Templates

**Using Templates**:
1. Browse available templates:
   - Meeting format sheet
   - Financial report template
   - GC agenda template
   - Service position description
   - Etc.
2. Click **Use Template**
3. Fill in blanks
4. Copy or print

**Adding Custom Templates**:
1. Click **Add Template**
2. Enter template name
3. Paste/type template content
4. Use {{placeholder}} for variables
5. Save

### Settings → General Settings

**Group Configuration**:
- Group name
- Meeting location
- Zoom meeting link
- Default meeting day/time

**Preferences**:
- Date format
- Time format (12/24 hour)
- Currency symbol
- Notification preferences

**Data Management**:
- **Export All Data**: Download complete backup
- **Import Data**: Restore from backup
- **Clear All Data**: Reset application (with confirmation)
- **Storage Usage**: See localStorage space used

### Settings → Accessibility

**Visual Adjustments**:
- Font size: Small, Medium, Large, Extra Large
- Contrast mode: Normal, High Contrast
- Color themes: Dark mode available

**Screen Reader Support**:
- Toggle screen reader optimization
- ARIA labels enabled
- Keyboard navigation support

**Keyboard Shortcuts**:
- Tab: Navigate form fields
- Enter: Submit forms/select items
- Esc: Close modals
- Arrow keys: Navigate calendar

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

### Regular Backups

**How Often**:
- **Weekly**: For active groups with frequent data entry
- **Monthly**: For less active groups
- **Before major changes**: Before importing data or major updates

**Backup Process**:
1. Go to **Settings** → **General Settings**
2. Scroll to **Data Management** section
3. Click **Export All Data**
4. Browser downloads a JSON file named `rowlett-group-backup-[date].json`
5. Store this file in multiple locations:
   - Cloud storage (Google Drive, Dropbox, OneDrive)
   - External USB drive
   - Email to group secretary
   - Shared group folder

**File Naming Convention**:
- Use date in filename: `rowlett-group-backup-2025-01-15.json`
- Include version if making multiple backups same day
- Keep last 3-6 months of backups

### Restoring from Backup

**When Needed**:
- Switched to new computer
- Accidentally cleared browser data
- Corrupted data
- Want to share data with another user

**Restore Process**:
1. Go to **Settings** → **General Settings**
2. Scroll to **Data Management** section
3. Click **Import Data**
4. Select backup JSON file
5. Choose import mode:
   - **Replace All**: Deletes current data, imports backup (recommended for fresh start)
   - **Merge**: Combines backup with current data (advanced - may create duplicates)
6. Confirm import
7. Page reloads with restored data

**Verification After Restore**:
1. Check **Home** dashboard for expected data
2. Spot-check several sections
3. Verify recent entries present
4. If issues, try different backup file

### Sharing Data Across Devices

**Method 1: Manual Transfer**:
1. Export data from Device A
2. Email/cloud share JSON file to yourself
3. Download on Device B
4. Import on Device B

**Method 2: Shared Backup Location**:
1. Export to shared cloud folder
2. On other device, download and import
3. Always export before importing to avoid conflicts

**Important**:
- Only one person should update data at a time
- Coordinate backups/imports to avoid overwriting
- Consider designating primary device for updates

### Storage Space Management

**Monitoring Usage**:
1. Go to **Settings** → **General Settings**
2. View **Storage Usage** section
3. Shows percentage of quota used

**If Running Low**:
1. **Export and Archive**:
   - Export old data
   - Delete old entries (>1 year)
   - Keep export for records
2. **Delete Large Items**:
   - Photo gallery uses most space
   - Consider external photo storage
   - Delete duplicate/unnecessary photos
3. **Clean Up**:
   - Delete test entries
   - Remove obsolete announcements
   - Archive old GC decisions

**Warnings**:
- **75% full**: Yellow warning
- **90% full**: Red alert, export data soon

---

## Maintenance

### Weekly Maintenance (Secretary/Chair)

**Review & Update**:
- ✅ Check upcoming meeting schedule
- ✅ Update any changed commitments
- ✅ Post new announcements
- ✅ Review and respond to messages
- ✅ Update service position changes

**Data Entry**:
- ✅ Log meeting attendance
- ✅ Record 7th tradition
- ✅ Update chip inventory after distributions
- ✅ Post photos from recent events

**Notifications**:
- ✅ Follow up on expiring service positions
- ✅ Confirm upcoming commitments
- ✅ Acknowledge upcoming birthdays

### Monthly Maintenance (Treasurer/Secretary)

**Financial**:
- ✅ Generate monthly financial report
- ✅ Review budget vs. actual
- ✅ Check prudent reserve status
- ✅ Reconcile 7th tradition totals
- ✅ Order chips if inventory low
- ✅ Export financial data for records

**Administrative**:
- ✅ Review service position terms
- ✅ Update any expired positions
- ✅ Archive old announcements
- ✅ Clean up messaging inbox

**Backup**:
- ✅ Export complete data backup
- ✅ Store in secure location
- ✅ Verify backup file integrity

### Quarterly Maintenance (Group)

**Data Review**:
- ✅ Review group analytics
- ✅ Generate attendance reports
- ✅ Assess engagement metrics
- ✅ Identify trends or concerns

**Content Update**:
- ✅ Update group history with recent milestones
- ✅ Review and update by-laws if needed
- ✅ Refresh document templates
- ✅ Update member roster (remove inactive)

**System Health**:
- ✅ Check browser compatibility
- ✅ Test on different devices
- ✅ Verify all features working
- ✅ Update bookmarks if needed

**Archive**:
- ✅ Export quarterly backup
- ✅ Archive old data if space low
- ✅ Clean photo gallery
- ✅ Remove obsolete templates

### Annual Maintenance (Group Conscience Decision)

**Comprehensive Review**:
- ✅ Full data audit
- ✅ Review all service positions
- ✅ Financial year-end reconciliation
- ✅ Update group information
- ✅ Review and vote on by-law changes

**Data Cleanup**:
- ✅ Archive data >2 years old
- ✅ Export archived data for records
- ✅ Clear test/duplicate entries
- ✅ Optimize photo storage

**Planning**:
- ✅ Set annual budget
- ✅ Plan service position rotation schedule
- ✅ Set contribution goals
- ✅ Update meeting format rotation

### Browser & System Updates

**When Browser Updates**:
1. Verify application still loads properly
2. Test key features (forms, calendar, exports)
3. If issues, try different browser
4. Check browser console for errors (F12)

**Switching Browsers**:
1. Export all data from old browser
2. Open application in new browser
3. Import data
4. Verify all features work
5. Update bookmarks

**Computer Replacement**:
1. Export data from old computer
2. Transfer backup file to new computer
3. Open `index.html` on new computer
4. Import backup data
5. Test functionality

---

## Troubleshooting

### Application Won't Load

**Possible Causes & Solutions**:

1. **Browser Issue**:
   - Try different browser (Chrome, Firefox, Edge, Safari)
   - Update browser to latest version
   - Clear browser cache: Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)

2. **JavaScript Disabled**:
   - Check browser settings
   - Enable JavaScript
   - Reload page

3. **File Corrupted**:
   - Re-download `index.html`
   - Ensure complete file (11,116 lines, ~500KB)

4. **Path Issues**:
   - Ensure `logo.svg` in same folder
   - Check file permissions
   - Try moving to different folder

### Data Not Saving

**Possible Causes & Solutions**:

1. **Private/Incognito Mode**:
   - Exit private browsing
   - Use normal browser window
   - localStorage disabled in private mode

2. **Storage Full**:
   - Check storage usage in Settings
   - Export and archive old data
   - Delete unnecessary photos

3. **Browser Restrictions**:
   - Check browser security settings
   - Allow localStorage for local files
   - Try different browser

4. **Form Validation**:
   - Check for required fields (marked *)
   - Ensure date formats correct
   - Look for error messages

### Features Not Working

**Calendar Not Showing Events**:
- Check date range selected
- Verify events saved properly
- Try refreshing page (F5)
- Check browser console for errors

**Photos Not Uploading**:
- Check file size (<5MB recommended)
- Use common formats (JPG, PNG, GIF)
- Check storage space available
- Try smaller images

**Export/Import Failed**:
- Ensure proper JSON file
- Check file not corrupted (open in text editor)
- Try exporting again
- Verify import mode selected

**Charts Not Displaying**:
- Ensure Chart.js library loaded
- Check internet connection (CDN resources)
- Try refreshing page
- Check browser console for errors

### Performance Issues

**Application Slow**:
1. **Too Much Data**:
   - Archive old entries
   - Reduce photo gallery size
   - Export and start fresh annually

2. **Browser Cache**:
   - Clear browser cache
   - Close unnecessary tabs
   - Restart browser

3. **Computer Resources**:
   - Close other applications
   - Check available RAM
   - Try simpler browser

**Forms Lagging**:
- Reduce number of members in dropdowns
- Archive inactive members
- Use search/filter functions

### Error Messages

**"localStorage quota exceeded"**:
- Storage full
- Export data
- Delete old entries
- Archive photos externally

**"Failed to parse JSON"**:
- Import file corrupted
- Try different backup
- Open JSON in text editor to verify format

**"Permission denied"**:
- Browser blocking localStorage
- Check security settings
- Try different browser
- Allow local file access

### Getting Help

**Check Browser Console**:
1. Press F12 (Windows) or Cmd+Option+I (Mac)
2. Click **Console** tab
3. Look for red error messages
4. Screenshot errors for troubleshooting

**Document the Issue**:
- What were you trying to do?
- What happened instead?
- Any error messages?
- Which browser/version?
- Recent changes to data/settings?

**Recovery Steps**:
1. Try refreshing page (F5)
2. Try different browser
3. Check for recent backup
4. Restore from backup if needed
5. Clear cache and try again

---

## Browser Compatibility

### Recommended Browsers

**Fully Tested & Supported**:
- ✅ Google Chrome 90+
- ✅ Microsoft Edge 90+
- ✅ Mozilla Firefox 88+
- ✅ Safari 14+

**Minimum Requirements**:
- JavaScript enabled
- localStorage support
- CSS3 support
- HTML5 support

### Mobile Browsers

**Supported**:
- ✅ Chrome Mobile (Android)
- ✅ Safari Mobile (iOS)
- ✅ Samsung Internet

**Notes**:
- Responsive design adapts to screen size
- Touch-friendly buttons and controls
- May need to rotate to landscape for tables
- Photo upload from camera supported

### Known Issues

**Internet Explorer**:
- ❌ Not supported
- Use Edge instead

**Very Old Browsers**:
- May have display issues
- Update to latest version
- Essential features should still work

---

## Security & Privacy

### Data Privacy

**Local Storage Only**:
- All data stored in browser localStorage
- Nothing sent to external servers
- No analytics or tracking
- No cookies except localStorage

**What This Means**:
- ✅ Complete privacy
- ✅ Offline functionality
- ✅ No internet required (after initial load)
- ❌ Data not automatically backed up
- ❌ Manual backup required
- ❌ Can't sync across devices automatically

### Best Practices

**Protect Your Data**:
1. **Regular Backups**:
   - Export weekly/monthly
   - Store in secure location
   - Don't rely solely on browser storage

2. **Access Control**:
   - Password-protect your computer
   - Lock screen when away
   - Don't use on public computers (data persists)

3. **Sensitive Information**:
   - Use discretion with personal details
   - Consider using first names only
   - Limit phone/email if desired
   - Follow AA anonymity tradition

**Sharing Backups**:
- Email only to trusted group members
- Use encrypted cloud storage
- Password-protect ZIP files if emailing
- Delete from shared locations after import

### XSS Protection

**Built-in Security**:
- DOMPurify library sanitizes all user input
- Prevents malicious script injection
- Safe to paste text from external sources

**Best Practice**:
- Still review what you paste
- Don't import JSON from untrusted sources
- Only restore backups you created

---

## Progressive Web App (PWA)

### Installing as App

**Desktop Installation** (Chrome/Edge):
1. Open application in browser
2. Look for install icon in address bar
3. Click **Install**
4. App installs as desktop application
5. Launch from Start Menu/Applications folder

**Mobile Installation** (iOS/Android):
1. Open in Safari (iOS) or Chrome (Android)
2. Tap Share button
3. Select "Add to Home Screen"
4. App icon appears on home screen

**Benefits**:
- Launches like native app
- Full-screen mode
- Faster access
- Works offline (after first load)
- App-like experience

---

## Tips & Best Practices

### For Group Secretary

1. **Establish Routine**:
   - Update attendance every meeting
   - Post announcements same day
   - Export data weekly
   - Review commitments day before meeting

2. **Communication**:
   - Use messaging for service reminders
   - Set announcement priorities appropriately
   - Follow up on action items promptly

3. **Documentation**:
   - Write detailed chairperson reports
   - Include action items with owners
   - Tag photos descriptively
   - Keep GC decisions detailed

### For Treasurer

1. **Accuracy**:
   - Log 7th tradition immediately after meetings
   - Keep receipts for all expenses
   - Reconcile monthly
   - Export financial reports for records

2. **Planning**:
   - Monitor prudent reserve monthly
   - Track chip inventory proactively
   - Watch for spending trends
   - Present clear reports at business meetings

3. **Budgeting**:
   - Set realistic budget categories
   - Review quarterly
   - Adjust based on actual spending
   - Plan for annual expenses (rent increases, etc.)

### For All Users

1. **Data Hygiene**:
   - Delete test entries
   - Archive old announcements
   - Keep member roster current
   - Remove duplicate photos

2. **Backup Discipline**:
   - Never skip backups
   - Store backups redundantly
   - Test restores occasionally
   - Document backup location

3. **Feature Utilization**:
   - Explore all sections
   - Use analytics for insights
   - Leverage templates for consistency
   - Utilize commitment reminders

4. **Continuous Improvement**:
   - Suggest features at group conscience
   - Customize templates for your group
   - Share usage tips with members
   - Refine processes based on experience

---

## Frequently Asked Questions

**Q: Can multiple people use this at the same time?**
A: Each person has their own copy in their browser. To share updates, one person should be designated to maintain the master copy and share exports regularly.

**Q: What happens if I clear my browser history?**
A: Clearing browsing data may delete localStorage. Always keep recent backups. You can restore from exported JSON file.

**Q: Can I use this on my phone?**
A: Yes! The application is responsive and works on mobile browsers. You can also install it as a PWA for app-like experience.

**Q: Do I need internet to use this?**
A: Only for the first load (to download CDN libraries like Chart.js). After that, it works completely offline.

**Q: How do I share data with incoming secretary?**
A: Export all data, share the JSON file with them, have them import it. Also share the `index.html` file.

**Q: Can I customize the colors/appearance?**
A: The CSS is embedded in `index.html`. Advanced users can edit the `<style>` section to customize colors and fonts.

**Q: What's the maximum number of members/events?**
A: Limited only by localStorage quota (~5MB). Typical groups can store years of data including hundreds of members and thousands of events.

**Q: Can I print from this application?**
A: Yes! Use browser print (Ctrl+P) or built-in export to PDF features in various sections. Print styles optimize for paper output.

**Q: Is my data encrypted?**
A: localStorage is not encrypted, but data never leaves your computer. Use computer password protection and disk encryption for additional security.

**Q: Can I use this for multiple groups?**
A: You'd need separate copies (different folders) or use different browsers. Each instance has its own localStorage.

---

## Support & Contribution

### Reporting Issues

If you encounter bugs or issues:
1. Check Troubleshooting section above
2. Verify browser compatibility
3. Try restoring from recent backup
4. Document error messages and steps to reproduce

### Feature Requests

This is an internal group tool. Discuss desired features at group conscience and customize as needed.

### Customization

The application is a single HTML file. Those with HTML/CSS/JavaScript knowledge can:
- Modify styles in `<style>` section
- Adjust layouts
- Add custom sections
- Customize terminology
- Change color scheme

**Before Customizing**:
1. Make backup copy of original `index.html`
2. Export all data
3. Test changes thoroughly
4. Document modifications

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

All libraries loaded via CDN - internet required for first load.

---

## Conclusion

This application is designed to serve your group for years with minimal maintenance. The key to success is:

1. **Regular backups** - Cannot be overstated
2. **Designated maintainer** - One person responsible
3. **Training** - Ensure continuity as service positions rotate
4. **Group conscience** - Decide as a group how to use it
5. **Tradition 12** - Anonymity at the level of press, radio, films, and the internet

Thank you for using this tool in service to your AA group!

---

**Last Updated**: January 2025
**Version**: 1.0
**For**: Rowlett Group Internal Use
