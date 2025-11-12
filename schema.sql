-- Personal Trainer App Database Schema
-- This schema should be run in your Supabase SQL Editor

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Profiles table (extends Supabase auth.users)
CREATE TABLE IF NOT EXISTS profiles (
    id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    role TEXT NOT NULL CHECK (role IN ('trainer', 'client')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Workouts table
CREATE TABLE IF NOT EXISTS workouts (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    trainer_id UUID REFERENCES profiles(id) ON DELETE CASCADE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    exercises JSONB, -- Array of exercise objects
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Meal plans table
CREATE TABLE IF NOT EXISTS meal_plans (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    trainer_id UUID REFERENCES profiles(id) ON DELETE CASCADE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    meals JSONB, -- Array of meal objects
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- Workout assignments table
CREATE TABLE IF NOT EXISTS workout_assignments (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    workout_id UUID REFERENCES workouts(id) ON DELETE CASCADE NOT NULL,
    client_id UUID REFERENCES profiles(id) ON DELETE CASCADE NOT NULL,
    assigned_date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    UNIQUE(workout_id, client_id, assigned_date)
);

-- Meal plan assignments table
CREATE TABLE IF NOT EXISTS meal_assignments (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    meal_plan_id UUID REFERENCES meal_plans(id) ON DELETE CASCADE NOT NULL,
    client_id UUID REFERENCES profiles(id) ON DELETE CASCADE NOT NULL,
    assigned_date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW()),
    UNIQUE(meal_plan_id, client_id, assigned_date)
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_workouts_trainer ON workouts(trainer_id);
CREATE INDEX IF NOT EXISTS idx_meal_plans_trainer ON meal_plans(trainer_id);
CREATE INDEX IF NOT EXISTS idx_workout_assignments_client_date ON workout_assignments(client_id, assigned_date);
CREATE INDEX IF NOT EXISTS idx_meal_assignments_client_date ON meal_assignments(client_id, assigned_date);

-- Row Level Security (RLS) Policies

-- Enable RLS on all tables
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE workouts ENABLE ROW LEVEL SECURITY;
ALTER TABLE meal_plans ENABLE ROW LEVEL SECURITY;
ALTER TABLE workout_assignments ENABLE ROW LEVEL SECURITY;
ALTER TABLE meal_assignments ENABLE ROW LEVEL SECURITY;

-- Profiles policies
CREATE POLICY "Users can view their own profile" ON profiles
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update their own profile" ON profiles
    FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Trainers can view all profiles" ON profiles
    FOR SELECT USING (
        EXISTS (
            SELECT 1 FROM profiles
            WHERE id = auth.uid() AND role = 'trainer'
        )
    );

-- Workouts policies
CREATE POLICY "Trainers can manage their own workouts" ON workouts
    FOR ALL USING (trainer_id = auth.uid());

CREATE POLICY "Clients can view workouts assigned to them" ON workouts
    FOR SELECT USING (
        EXISTS (
            SELECT 1 FROM workout_assignments
            WHERE workout_assignments.workout_id = workouts.id
            AND workout_assignments.client_id = auth.uid()
        )
    );

-- Meal plans policies
CREATE POLICY "Trainers can manage their own meal plans" ON meal_plans
    FOR ALL USING (trainer_id = auth.uid());

CREATE POLICY "Clients can view meal plans assigned to them" ON meal_plans
    FOR SELECT USING (
        EXISTS (
            SELECT 1 FROM meal_assignments
            WHERE meal_assignments.meal_plan_id = meal_plans.id
            AND meal_assignments.client_id = auth.uid()
        )
    );

-- Workout assignments policies
CREATE POLICY "Trainers can manage workout assignments" ON workout_assignments
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM workouts
            WHERE workouts.id = workout_assignments.workout_id
            AND workouts.trainer_id = auth.uid()
        )
    );

CREATE POLICY "Clients can view their own workout assignments" ON workout_assignments
    FOR SELECT USING (client_id = auth.uid());

CREATE POLICY "Clients can update their own workout completion" ON workout_assignments
    FOR UPDATE USING (client_id = auth.uid());

-- Meal assignments policies
CREATE POLICY "Trainers can manage meal assignments" ON meal_assignments
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM meal_plans
            WHERE meal_plans.id = meal_assignments.meal_plan_id
            AND meal_plans.trainer_id = auth.uid()
        )
    );

CREATE POLICY "Clients can view their own meal assignments" ON meal_assignments
    FOR SELECT USING (client_id = auth.uid());

CREATE POLICY "Clients can update their own meal completion" ON meal_assignments
    FOR UPDATE USING (client_id = auth.uid());

-- Function to automatically create profile on signup
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.profiles (id, email, role)
    VALUES (NEW.id, NEW.email, 'client'); -- Default role is client
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger to call the function on new user signup
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
