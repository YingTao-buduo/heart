function getHeartRate(heartbeatFrameData, fps) {
    var totalInterval = heartbeatFrameData[heartbeatFrameData.length - 1] - heartbeatFrameData[0];
    var avgInterval = totalInterval / (heartbeatFrameData.length - 1);
    var heartRate = fps * 60 / avgInterval;
    return heartRate;
}

export default getHeartRate;
