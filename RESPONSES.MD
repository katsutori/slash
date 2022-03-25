# Think of a recent time you worked on a performance problem or bug in production.
### `Write a paragraph about it, in technical detail of how you figured out what the problem was and resolved it.`
Several developers were working on a social media application that allowed users to follow others users. When a user is on another user's profile and clicks on the Follow button, an entry is written into the database under a join table and the follow button changes to an Unfollow button. When the Unfollow button is clicked, the existing follow entry in the database is destroyed.

When a user rapidly clicks the Follow/Unfollow buttons, a race condition occurs where either the database will create multiple follow entries for the same paired users or attempt to destroy entries that do not exist. When multiple entries exists for the same paired users, the database sends back a 500 response and is no longer capable of handling requests for those specific instances of users.

To address this issue, I wrote iterations and conditionals to check if the logged in user's following list has an entry that consists of the user that the logged in user is attempting to follow. If none exists, an entry is created when a boolean changes and triggers a conditional. Otherwise, a message is sent to the user asking them to try again. The same logic was applied to unfollowing users.

### `Write another paragraph about it, as if you were explaining to your manager in less-technical but still meaningful terminology.`
The former endpoints allowed users to abuse the follow and unfollow buttons, so I added some conditionals into the follow and unfollow endpoints that checked for a preexisting entry. If an entry already existed, I prevented the database from creating another entry until the former was first removed. EZPZ.
