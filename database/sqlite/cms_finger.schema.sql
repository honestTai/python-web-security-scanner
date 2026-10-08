-- SQLite schema extracted without original records.
CREATE TABLE cms
        (id INT PRIMARY KEY     NOT NULL,
        cms_name           TEXT    NOT NULL,
        path            INT     NOT NULL,
        match_pattern   TEXT NOT NULL,
        options   TEXT NOT NULL
        );
CREATE TABLE fofa_cms
        (id INT PRIMARY KEY     NOT NULL,
        name           TEXT    NOT NULL,
        keys            INT     NOT NULL
        );
