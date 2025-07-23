from core.voice import recognize_and_respond

if __name__ == "__main__":
    print("[System] DUO_HARMONY starting. Press Ctrl+C to exit.")
    while True:
        try:
            recognize_and_respond()
        except KeyboardInterrupt:
            print("\n[System] Exiting DUO_HARMONY.")
            break
