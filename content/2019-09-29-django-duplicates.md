date: 2019-09-29
layout: post
title: How to find and handle duplicate rows in Django
description: How to find and handle duplicate rows in Django using "group by" query
tags: 'python'
code: true
draft: true

Sometimes we have duplicate rows in database due to some bad design or schema change. Lets see how we can fix them.

**Algorithm**

- The solution is to "group by" rows based on the required columns.
- Add a column for counts
- Filter rows where count is more than 1

Lets say we have a model `Announcement` with `company_id` (FK), `title`, `broadcast_date` and other fields. We want to delete duplicate announcements for the company on same date.

```python
from django.db.models import Min, Max, Count
from documents.models import Announcement

# Groupby by putting group identifiers in values
# then annotate a count record
dupes = Announcement.objects.values('company_id', 'title', 'broadcast_date') \
    .order_by() \
    .annotate(
        first_update_id=Min('id'),
        records=Count('id'),
    ).filter(
        records__gt=1
    )

# Check query
print dupes.query

# Handle duplicate
for result in dupes:
    Announcement.objects.filter(
        company_id=result['company_id'],
        title=report['title'],
        broadcast_date=report['broadcast_date'],
    ).exclude(id=report['first_update_id']).delete()
```

**Using `unique` and `unique_together` database constraints**

Best way to handle duplicates is to use `unique` or `unique_together` constraints at  database level. A common error is sometimes to use a *nullable* field in `unique_together`. In SQL, `null` is not equal to anything. In-fact, `null` is not equal to even `null`. So a `unique` constraint on a `null` value won't work.
