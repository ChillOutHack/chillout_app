-- Table: events

-- DROP TABLE events;

CREATE TABLE events
(
  type integer,
  skin_temp double precision,
  time_stamp datetime,
  peltier_temp double precision,
  delta_temp double precision
);