# Dimensions & Metrics

Analytics Help ([링크](https://support.google.com/analytics/answer/13947485?hl=en&sjid=11583338961725404950-AP&visit_id=638677731624404168-688281417&ref_topic=13948007&rd=1))

[toc]

## Sessions

> A period during which a user is engaged with the website or app.

- **Start**: when a user either opens app in the foreground or views a page/screen and no session is currently active
    - Google automatically (1) collects a `session_start` event and (2) generates a session ID(`ga_session_id`) and session number(`ga_session_number`) via the `session_start` event.
- **End**: after 30 mins of user inactivity
- **Caclulation**: by estimating the num of *unique session IDs*

## Engagement Rate & Bounce Rate

- **Engagement Rate**: % of engaged sessions

- **Bounce Rate**: % of sessionsthat were not engaged

## Entrances & Exits

- **Entrances**: # of times the first event in a session happened on a page/screen
- **Exits**: shows how many times the last event in a session happened on a page/screen