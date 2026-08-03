CREATE TABLE IF NOT EXISTS user_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL UNIQUE,
    total_study_minutes INT DEFAULT 0,
    completed_quizzes_count INT DEFAULT 0,
    current_level VARCHAR(50) DEFAULT 'Novice Historian',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_bookmarks (
    bookmark_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    item_id VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);