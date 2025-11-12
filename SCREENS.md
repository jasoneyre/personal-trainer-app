# Application Screens Overview

This document describes the user interface screens in the Personal Trainer MVP.

---

## 🔐 Authentication Screens

### Login/Signup Page
**URL:** Initial page when not logged in

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  💪 Personal Trainer App                            │
├─────────────────────────────────────────────────────┤
│  [Login Tab] [Sign Up Tab]                          │
│                                                      │
│  Login Tab:                                         │
│  ┌─────────────────────────────────────────┐       │
│  │ Email:    [__________________]          │       │
│  │ Password: [__________________]          │       │
│  │                                         │       │
│  │           [Login Button]                │       │
│  └─────────────────────────────────────────┘       │
│                                                      │
│  Sign Up Tab:                                       │
│  ┌─────────────────────────────────────────┐       │
│  │ Email:     [__________________]         │       │
│  │ Password:  [__________________]         │       │
│  │ Full Name: [__________________]         │       │
│  │ I am a:    [▼ client/trainer]          │       │
│  │                                         │       │
│  │           [Sign Up Button]              │       │
│  └─────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────┘
```

---

## 👨‍🏫 Trainer Screens

### Trainer Dashboard - Workout Management
**Navigation:** Workouts (sidebar)

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  👋 Welcome, Sarah Johnson                          │
├──────────┬──────────────────────────────────────────┤
│ Sidebar  │  💪 Workout Management                   │
│          │                                           │
│ [Logout] │  ▼ ➕ Create New Workout                 │
│          │  ┌────────────────────────────────────┐  │
│ •Workouts│  │ Workout Title: [____________]      │  │
│ •Meals   │  │ Description:  [____________]       │  │
│ •Assign  │  │                                    │  │
│          │  │ Exercises:                         │  │
│          │  │ Number of exercises: [3]           │  │
│          │  │                                    │  │
│          │  │ Exercise 1                         │  │
│          │  │ Name:[______] Sets:[__] Reps:[__] │  │
│          │  │                                    │  │
│          │  │ Exercise 2                         │  │
│          │  │ Name:[______] Sets:[__] Reps:[__] │  │
│          │  │                                    │  │
│          │  │ Exercise 3                         │  │
│          │  │ Name:[______] Sets:[__] Reps:[__] │  │
│          │  │                                    │  │
│          │  │        [Create Workout]            │  │
│          │  └────────────────────────────────────┘  │
│          │                                           │
│          │  Existing Workouts:                      │
│          │  ▼ 📋 Full Body Strength                 │
│          │  ▼ 📋 Cardio Blast                       │
│          │  ▼ 📋 Upper Body Focus                   │
└──────────┴──────────────────────────────────────────┘
```

### Trainer Dashboard - Meal Plan Management
**Navigation:** Meal Plans (sidebar)

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  👋 Welcome, Sarah Johnson                          │
├──────────┬──────────────────────────────────────────┤
│ Sidebar  │  🍽️ Meal Plan Management                 │
│          │                                           │
│ [Logout] │  ▼ ➕ Create New Meal Plan               │
│          │  ┌────────────────────────────────────┐  │
│ •Workouts│  │ Title:       [____________]        │  │
│ •Meals   │  │ Description: [____________]        │  │
│ •Assign  │  │                                    │  │
│          │  │ Meals:                             │  │
│          │  │ Number of meals: [3]               │  │
│          │  │                                    │  │
│          │  │ Meal 1                             │  │
│          │  │ Name:[_____] Time:[_______]       │  │
│          │  │ Items: [__________________]        │  │
│          │  │                                    │  │
│          │  │ Meal 2                             │  │
│          │  │ Name:[_____] Time:[_______]       │  │
│          │  │ Items: [__________________]        │  │
│          │  │                                    │  │
│          │  │        [Create Meal Plan]          │  │
│          │  └────────────────────────────────────┘  │
│          │                                           │
│          │  Existing Meal Plans:                    │
│          │  ▼ 🍽️ Balanced Day                       │
│          │  ▼ 🍽️ High Protein Plan                  │
└──────────┴──────────────────────────────────────────┘
```

### Trainer Dashboard - Client Assignment
**Navigation:** Assign to Clients (sidebar)

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  👋 Welcome, Sarah Johnson                          │
├──────────┬──────────────────────────────────────────┤
│ Sidebar  │  📅 Assign to Clients                    │
│          │                                           │
│ [Logout] │  [Assign Workout] [Assign Meal Plan]     │
│          │                                           │
│ •Workouts│  Assign Workout Tab:                     │
│ •Meals   │  ┌────────────────────────────────────┐  │
│ •Assign  │  │ Select Client:                     │  │
│          │  │ [▼ Mike Thompson (mike@...)]       │  │
│          │  │                                    │  │
│          │  │ Select Workout:                    │  │
│          │  │ [▼ Full Body Strength]            │  │
│          │  │                                    │  │
│          │  │ Date:                              │  │
│          │  │ [📅 11/12/2025]                    │  │
│          │  │                                    │  │
│          │  │     [Assign Workout]               │  │
│          │  └────────────────────────────────────┘  │
│          │                                           │
│          │  Assign Meal Plan Tab:                   │
│          │  ┌────────────────────────────────────┐  │
│          │  │ Select Client:                     │  │
│          │  │ [▼ Mike Thompson (mike@...)]       │  │
│          │  │                                    │  │
│          │  │ Select Meal Plan:                  │  │
│          │  │ [▼ Balanced Day]                   │  │
│          │  │                                    │  │
│          │  │ Date:                              │  │
│          │  │ [📅 11/12/2025]                    │  │
│          │  │                                    │  │
│          │  │     [Assign Meal Plan]             │  │
│          │  └────────────────────────────────────┘  │
└──────────┴──────────────────────────────────────────┘
```

---

## 🏋️ Client Screens

### Client Dashboard - Today's Checklist
**Navigation:** Automatic on login

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  👋 Welcome, Mike Thompson                          │
├──────────┬──────────────────────────────────────────┤
│ Sidebar  │  📅 Today's Checklist                    │
│          │  Date: Tuesday, November 12, 2025        │
│ [Logout] │                                           │
│          │  💪 Workouts                             │
│          │                                           │
│          │  ▼ ⬜ Full Body Strength                 │
│          │  ┌────────────────────────────────────┐  │
│          │  │ Description: Beginner-friendly     │  │
│          │  │                                    │  │
│          │  │ Exercises:                         │  │
│          │  │ 1. Squats - 3 sets x 12 reps      │  │
│          │  │ 2. Push-ups - 3 sets x 10 reps    │  │
│          │  │ 3. Lunges - 3 sets x 10 each...   │  │
│          │  │ 4. Plank - 3 sets x 30 seconds... │  │
│          │  │                                    │  │
│          │  │ ☐ Mark as complete                │  │
│          │  └────────────────────────────────────┘  │
│          │                                           │
│          │  ▼ ✅ Cardio Blast                       │
│          │  (Collapsed - completed)                 │
│          │                                           │
│          │  🍽️ Meal Plans                           │
│          │                                           │
│          │  ▼ ⬜ Balanced Day                        │
│          │  ┌────────────────────────────────────┐  │
│          │  │ Description: Well-rounded...       │  │
│          │  │                                    │  │
│          │  │ Meals:                             │  │
│          │  │ 1. Breakfast (7:00 AM)            │  │
│          │  │    Oatmeal with berries, 2 eggs   │  │
│          │  │ 2. Lunch (12:00 PM)               │  │
│          │  │    Grilled chicken salad, quinoa  │  │
│          │  │ 3. Dinner (6:00 PM)               │  │
│          │  │    Salmon, sweet potato, broccoli │  │
│          │  │                                    │  │
│          │  │ ☐ Mark as complete                │  │
│          │  └────────────────────────────────────┘  │
└──────────┴──────────────────────────────────────────┘
```

### Client Dashboard - Empty State
**When no assignments for today:**

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  👋 Welcome, Mike Thompson                          │
├──────────┬──────────────────────────────────────────┤
│ Sidebar  │  📅 Today's Checklist                    │
│          │  Date: Tuesday, November 12, 2025        │
│ [Logout] │                                           │
│          │  💪 Workouts                             │
│          │  ℹ️ No workouts assigned for today.      │
│          │                                           │
│          │  🍽️ Meal Plans                           │
│          │  ℹ️ No meal plans assigned for today.    │
└──────────┴──────────────────────────────────────────┘
```

---

## 🎨 UI Elements Reference

### Icons Used:
- 💪 - Workouts
- 🍽️ - Meal Plans
- 👋 - Welcome message
- 📅 - Calendar/Date
- 📋 - Workout item
- ✅ - Completed item
- ⬜ - Incomplete item
- ➕ - Create new
- ▼ - Expandable section (collapsed)
- ▲ - Expandable section (expanded)
- ℹ️ - Information message

### Color Scheme (Streamlit defaults):
- Primary: Blue (#FF4B4B)
- Success: Green
- Info: Blue
- Warning: Orange
- Error: Red

### Interactive Elements:
- **Text Input:** Single-line text entry
- **Text Area:** Multi-line text entry
- **Select Box:** Dropdown menu
- **Date Input:** Calendar picker
- **Checkbox:** Boolean toggle
- **Button:** Action trigger
- **Expander:** Collapsible section
- **Tabs:** Switchable views

---

## 🔄 User Flows

### Trainer Creates and Assigns Workout:
```
Login → Workouts → Create New Workout → Fill Details → 
Create → Assign to Clients → Select Client/Workout/Date → 
Assign → Success!
```

### Client Completes Daily Tasks:
```
Login → See Today's Checklist → Expand Workout → 
Read Exercises → Complete Workout → Check "Mark as complete" → 
Item marked with ✅
```

### Multi-Day Planning:
```
Trainer: Create Workout → Assign to Client (Date: Monday) → 
Assign to Client (Date: Tuesday) → ... repeat for week

Client: Monday - See Monday's workout
        Tuesday - See Tuesday's workout (different from Monday)
```

---

## 📱 Responsive Design

The application is built with Streamlit which provides responsive design out of the box:

- **Desktop:** Full sidebar navigation, wide content area
- **Tablet:** Collapsible sidebar, adjusted spacing
- **Mobile:** Hamburger menu sidebar, stacked layout

---

## 🎯 Key UX Features

1. **Clear Visual Hierarchy:** Important actions are prominent
2. **Immediate Feedback:** Success/error messages on every action
3. **Progressive Disclosure:** Expandable sections hide complexity
4. **Consistent Icons:** Same icons used throughout for recognition
5. **Logical Grouping:** Related features grouped together
6. **Minimal Clicks:** Most actions in 2-3 clicks
7. **No Dead Ends:** Always clear next action
8. **Error Prevention:** Form validation before submission

---

## 🔮 Future UI Enhancements

- Calendar view for multi-day planning
- Drag-and-drop exercise ordering
- Progress charts and graphs
- Photo uploads for exercises
- Dark mode toggle
- Custom branding/themes
- Mobile native app
- Offline mode

---

**End of Screens Documentation**
