import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(0, 0, "Press q to exit")

    userlist_w = 10
    win_userlist = stdscr.derwin(
        curses.LINES - 2, userlist_w - 1, 0, 0)
    win_chatline = stdscr.derwin(
        curses.LINES - 1, 0)
    
    h, w = stdscr.getmaxyx()
    u_h, u_w = win_userlist.getmaxyx()
    stdscr.clear()
    stdscr.vline(0, u_w + 1, '|', h - 2)
    stdscr.hline(h-2, 0, '-', w)
    stdscr.refresh()

    win_userlist.clear()
    win_userlist.addstr(0, 0, "aaa")
    win_userlist.addstr(1, 0, "bb")
    win_userlist.refresh()

    
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            return

wrapper(main)