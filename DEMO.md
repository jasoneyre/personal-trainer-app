# Application Demo Script

This script demonstrates how to use the Personal Trainer App in a real-world scenario.

## Prerequisites
- Supabase project set up with schema.sql executed
- .env file configured with your Supabase credentials
- Application running via `streamlit run app.py`

## Demo Scenario: "FitPro Personal Training"

### Characters:
- **Sarah (Trainer)** - Personal trainer who wants to manage her clients
- **Mike (Client)** - Client who needs a workout and meal plan

---

## Part 1: Trainer Setup (Sarah)

### Step 1: Sign Up as Trainer
1. Open the application in browser
2. Click "Sign Up" tab
3. Fill in:
   - Email: sarah@fitpro.com
   - Password: SecurePass123!
   - Full Name: Sarah Johnson
   - Role: **trainer**
4. Click "Sign Up"
5. Check email and verify account
6. Log in with credentials

### Step 2: Create Workouts
1. After login, navigate to "Workouts" in sidebar
2. Click "Create New Workout" expander

**Workout 1: Full Body Strength**
- Title: Full Body Strength
- Description: Beginner-friendly full body workout
- Exercises:
  - Exercise 1: Squats | 3 | 12
  - Exercise 2: Push-ups | 3 | 10
  - Exercise 3: Lunges | 3 | 10 each leg
  - Exercise 4: Plank | 3 | 30 seconds
- Click "Create Workout"

**Workout 2: Cardio Blast**
- Title: Cardio Blast
- Description: High-intensity cardio session
- Exercises:
  - Exercise 1: Jumping Jacks | 3 | 20
  - Exercise 2: Burpees | 3 | 10
  - Exercise 3: Mountain Climbers | 3 | 15
- Click "Create Workout"

### Step 3: Create Meal Plans
1. Navigate to "Meal Plans" in sidebar
2. Click "Create New Meal Plan" expander

**Meal Plan: Balanced Day**
- Title: Balanced Day
- Description: Well-rounded nutrition for training days
- Meals:
  - Meal 1: Breakfast | 7:00 AM | Oatmeal with berries, 2 eggs, green tea
  - Meal 2: Lunch | 12:00 PM | Grilled chicken salad, quinoa, olive oil dressing
  - Meal 3: Dinner | 6:00 PM | Salmon, sweet potato, steamed broccoli
  - Meal 4: Snack | 3:00 PM | Greek yogurt with almonds
- Click "Create Meal Plan"

---

## Part 2: Client Setup (Mike)

### Step 1: Sign Up as Client
1. Open application in new browser (or incognito window)
2. Click "Sign Up" tab
3. Fill in:
   - Email: mike@example.com
   - Password: MyPass456!
   - Full Name: Mike Thompson
   - Role: **client**
4. Click "Sign Up"
5. Check email and verify account
6. Log in with credentials

### Step 2: View Today's Checklist
1. After login, see "Today's Checklist" page
2. Currently shows:
   - "No workouts assigned for today"
   - "No meal plans assigned for today"

---

## Part 3: Trainer Assigns to Client (Sarah)

### Step 1: Assign Workout
1. Log back in as Sarah (trainer)
2. Navigate to "Assign to Clients" in sidebar
3. Click "Assign Workout" tab
4. Fill in:
   - Select Client: Mike Thompson (mike@example.com)
   - Select Workout: Full Body Strength
   - Date: Today's date
5. Click "Assign Workout"
6. See success message

### Step 2: Assign Meal Plan
1. Stay in "Assign to Clients" page
2. Click "Assign Meal Plan" tab
3. Fill in:
   - Select Client: Mike Thompson (mike@example.com)
   - Select Meal Plan: Balanced Day
   - Date: Today's date
4. Click "Assign Meal Plan"
5. See success message

---

## Part 4: Client Completes Tasks (Mike)

### Step 1: View Assignments
1. Log back in as Mike (client)
2. Refresh the page or navigate away and back
3. Now see:
   - ⬜ Full Body Strength (workout)
   - ⬜ Balanced Day (meal plan)

### Step 2: Complete Workout
1. Click on "⬜ Full Body Strength" to expand
2. See all exercises:
   - Squats - 3 sets x 12 reps
   - Push-ups - 3 sets x 10 reps
   - Lunges - 3 sets x 10 each leg reps
   - Plank - 3 sets x 30 seconds reps
3. After completing workout, check "Mark as complete"
4. Expander now shows "✅ Full Body Strength"

### Step 3: Complete Meal Plan
1. Click on "⬜ Balanced Day" to expand
2. See all meals:
   - Breakfast (7:00 AM): Oatmeal with berries, 2 eggs, green tea
   - Lunch (12:00 PM): Grilled chicken salad, quinoa, olive oil dressing
   - Dinner (6:00 PM): Salmon, sweet potato, steamed broccoli
   - Snack (3:00 PM): Greek yogurt with almonds
3. After following the meal plan, check "Mark as complete"
4. Expander now shows "✅ Balanced Day"

---

## Part 5: Multi-Day Planning (Sarah)

### Assign Week's Worth of Workouts
1. Log in as Sarah (trainer)
2. Navigate to "Assign to Clients"
3. Assign workouts for the next 7 days:
   - Monday: Full Body Strength
   - Tuesday: Cardio Blast
   - Wednesday: Full Body Strength
   - Thursday: Cardio Blast
   - Friday: Full Body Strength
   - Saturday: Cardio Blast
   - Sunday: (Rest day - no assignment)

### Mike's Experience
1. Each day, Mike logs in
2. Only sees TODAY's assignments
3. Marks them complete as he finishes
4. Tomorrow's assignments appear tomorrow

---

## Expected Results

### For Trainer (Sarah):
- ✓ Can create multiple workouts
- ✓ Can create multiple meal plans
- ✓ Can see all registered clients
- ✓ Can assign any workout/meal to any client for any date
- ✓ Can delete workouts and meal plans

### For Client (Mike):
- ✓ Can only see assignments for today's date
- ✓ Can mark workouts as complete
- ✓ Can mark meals as complete
- ✓ Completed items show with ✅
- ✓ Incomplete items show with ⬜
- ✓ Cannot see other clients' data
- ✓ Cannot create or delete workouts/meals

---

## Testing Edge Cases

### Test 1: Multiple Clients
1. Create another client account (jane@example.com)
2. Assign different workouts to Mike and Jane for the same date
3. Verify each client only sees their own assignments

### Test 2: Past and Future Dates
1. Assign a workout to Mike for tomorrow
2. Check that Mike doesn't see it today
3. Come back tomorrow and verify it appears

### Test 3: Multiple Assignments
1. Assign 2 different workouts to Mike for the same day
2. Verify both appear in Mike's checklist
3. Verify Mike can complete them independently

### Test 4: Deletion
1. Create a workout as Sarah
2. Assign it to Mike for tomorrow
3. Delete the workout
4. Verify assignment is also removed (due to CASCADE)

---

## Tips for Demo

1. **Use Two Browsers**: One for trainer, one for client
2. **Today's Date**: Always use today's date for assignments to see immediate results
3. **Refresh**: Remember to refresh/rerun after making changes
4. **Unique Emails**: Each user needs a unique email address
5. **Email Verification**: Check spam folder if verification email doesn't arrive

---

## Success Criteria

✅ Trainer can create workouts
✅ Trainer can create meal plans
✅ Trainer can assign to clients by date
✅ Client sees "Today" view only
✅ Client can mark items complete
✅ Authentication works
✅ Role-based access works
✅ Data is isolated per user (RLS)

---

## Troubleshooting Demo Issues

**Issue**: "No clients registered yet"
- **Solution**: Make sure Mike (client) has signed up first

**Issue**: Client doesn't see assignments
- **Solution**: Check that assignment date matches today's date

**Issue**: Can't log in
- **Solution**: Check email for verification link

**Issue**: Database errors
- **Solution**: Verify schema.sql was executed in Supabase

---

**Demo Complete!** 🎉

The application successfully demonstrates all MVP requirements:
- Trainers can create and manage content
- Trainers can assign to clients by date
- Clients see a "Today" checklist
- Clients can mark items complete
