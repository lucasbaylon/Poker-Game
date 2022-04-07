import queue
import threading

game_event = threading.Event()
response_q = queue.Queue()
game_info_q = queue.Queue()
