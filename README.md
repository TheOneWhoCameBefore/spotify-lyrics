# spotify-lyrics
A simple program using the spotify and musixmatch APIs to get the current line of lyrics for the currently playing song.

Note: Musixmatch is gonna make me pay so I guess we can't use them. Ah well.

TODO:
 - Research using spclient.wg.spotify.com for lyrics
 - Implement a local clock which syncs with timestamp of song every 5 seconds (avoid spamming spotify api and also continueous lyric matching)
 - Error handling for ads, no current song playing, etc.
 - Determine what to do with long periods of instrumental (how to identify etc.)
 - Check if user has authenticated or not (maybe if tokens exists?) and prompt them if not
 - Confirm tokens will refresh over long periods of time
 - Check command line functionality
 - Oraginze and structure (currently very prototype, mostly proof of concept)