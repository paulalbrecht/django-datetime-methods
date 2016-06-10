Example implementations of calculating due date and how overdue it is. Specifically with output "Green", "Yellow", or "Red" depending on the number of days.

I wanted to play around with the different implenetations and see if there was a clear winner in terms of speed/readability/ease and look into profiling

Template tag: use a template tag to if/else return based on the calculated date from now()
ExpressionWrapper:  use an expressionwrapper to output a durationfield and then if/else that in the template itself
Case/When: use the queryset Case/When to output the text value directly.
