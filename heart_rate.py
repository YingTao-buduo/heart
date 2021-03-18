def get_heart_rate(heart_rate_frame_data, fps):
    print('Begin HR')
    total_interval = heart_rate_frame_data[len(heart_rate_frame_data) - 1] - heart_rate_frame_data[0]
    avg_interval = total_interval / len(heart_rate_frame_data[1:])
    print('HR OK')
    return fps * 60 / avg_interval
