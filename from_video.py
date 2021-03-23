def get_video_frames(cap):

    data = []
    print('Begin to read frames from video')
    while True:
        try:
            ret, frame = cap.read()
            if frame is not None:
                data.append(frame)
            else:
                break
        except Exception as e:
            print(e)
            break

    print('Getting frames from video OK')
    return data
