# ETL Pipeline Design

## Extract
Load raw event data from CSV. In a real setting this could be replaced by an API, cloud storage bucket, or database source.

## Transform
- Standardize column names.
- Parse timestamps.
- Convert numeric values.
- Remove invalid timestamps and missing user IDs.
- Remove duplicate events.
- Add analytical fields such as event date and revenue-event flag.

## Validate
- Required columns must exist.
- Event IDs must be unique.
- User IDs must not be null after cleaning.

## Load
Write clean event data and daily event summaries to processed CSV files. A SQL schema is included for warehouse-style loading.
