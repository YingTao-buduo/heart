function getRedFromRGBa(frameDatum){
    sum_red = 0;
    for(var i = 0; i < frameDatum.length; i += 4){
        sum_red += frameDatum[i];
    }
    return sum_red;
}

module.exports = getRedFromRGBa;