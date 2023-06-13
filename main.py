import streamlit as st
import pandas as pd
import numpy as np
import datetime
import os
import pickle
import hashlib
import uuid
import random
if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists("data/boards.pkl"):
    with open("data/boards.pkl", "wb") as f:
        pickle.dump({}, f)

if not os.path.exists("data/threads.pkl"):
    with open("data/threads.pkl", "wb") as f:
        pickle.dump({}, f)

if not os.path.exists("data/users.pkl"):
    with open("data/users.pkl", "wb") as f:
        pickle.dump([], f)
with open("data/boards.pkl", "rb") as f:
    boards = pickle.load(f)

with open("data/threads.pkl", "rb") as f:
    threads = pickle.load(f)

with open("data/users.pkl", "rb") as f:
    users = pickle.load(f)
board_names = list(boards.keys())
board = st.sidebar.selectbox("Select board", board_names)

if st.sidebar.button("New board"):
    new_board_name = st.sidebar.text_input("Enter board name")
    if new_board_name != "" and new_board_name not in board_names:
        boards[new_board_name] = []
        with open("data/boards.pkl", "wb") as f:
            pickle.dump(boards, f)
        board_names.append(new_board_name)
        board = new_board_name

if board not in boards:
    st.error("Board not found.")
    st.stop()
threads_in_board = [threads[thread_id] for thread_id in boards[board]]
for thread in threads_in_board:
    st.write(f"Thread: {thread['title']} ({thread['created_at']})")
if st.button("New Thread"):
    thread_title = st.text_input("Thread Title")
    thread_content = st.text_area("Thread Content")
    if thread_title != "" and thread_content != "":
        thread_id = str(uuid.uuid4())
        user_id = random.randint(1, len(users))
        thread = {
            "id": thread_id,
            "title": thread_title,
            "content": thread_content,
            "created_by": users[user_id-1]["username"],
            "created_at": str(datetime.datetime.now()),
            "board": board,
            "comments": []
        }
        threads[thread_id] = thread
        boards[board].append(thread_id)
        with open("data/threads.pkl", "wb") as f:
            pickle.dump(threads, f)
        with open("data/boards.pkl", "wb") as f:
            pickle.dump(boards, f)
        st.success("Thread created.")
    else:
        st.error("Please enter a title and content.")
