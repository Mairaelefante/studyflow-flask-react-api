CREATE TABLE clean_events (
    event_id INTEGER PRIMARY KEY,
    event_time TIMESTAMP NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    value NUMERIC(10, 2),
    source VARCHAR(50),
    event_date DATE,
    is_revenue_event BOOLEAN
);

CREATE INDEX idx_clean_events_date ON clean_events(event_date);
CREATE INDEX idx_clean_events_user ON clean_events(user_id);
CREATE INDEX idx_clean_events_type ON clean_events(event_type);
