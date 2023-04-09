# Anubis

This is a simple discord bot, meant to generate statistics for reactions on posts.

Well-suited for a server I frequent that often has users reacting with various emoji based on their opinion of a post.

## Commands

All commands are prefixed with `!`

- `reactions_received @user num_posts [channel]`
  - Scans `channel`'s history, up to `num_posts` amount. For each post by `user`, record the reactions that post received. Sends a message to the channel the command was sent in with summary statistics. If `channel` is not specified (either as a channel mention or the channel name), it defaults to scanning the channel the command was sent in.
- `reactions_given @user num_posts [channel]`
  - Similar to above, except gathers statistics on reactions `user` gave to posts (including their own).
  - Significantly more network-intense due to needing to request both message history, and list of users from Discord for each group of reactions.

## Future ideas

1. Scan for and return a post with the most reactions total, or most of a specific emoji
2. Have the bot display a typing indicator while processing
3. Return posts with high reactions that do not have an embed (for conversations that have high interaction)
