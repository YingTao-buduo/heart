function polyfit(userInput) {
    var returnResult = [];
    var n = userInput.length;
    var inputMatrix = [];

    // Change the user input array to input matrix below

    /**
     * | a1 b1 c1 ... r1 |
     * | a1 b2 c2 ... r2 |
     * |      ......     |
     * | an bn cn ... rn |
     */
    for (var i = 0; i < n; i++) {
        var tempArr = [];
        for (var j = 0; j < n; j++) {
            tempArr.push(Math.pow(userInput[i].x, n - j - 1));
        }
        tempArr.push(userInput[i].y);
        inputMatrix.push(tempArr);
    }

    // 高斯消元法 通过矩阵初等变换,将输入矩阵变为如下形式

    /**
     * | 1 0 0 ... 0 r1 |
     * | 0 1 0 ... 0 r2 |
     * |      ......    |
     * | 0 0 0 ... 1 rn |
     */

    for (var i = 0; i < n; i++) {
        var base = inputMatrix[i][i];

        for (var j = 0; j < n + 1; j++) {
            inputMatrix[i][j] = inputMatrix[i][j] / base;
        }

        for (var j = 0; j < n; j++) {
            if (i != j) {
                var baseInner = inputMatrix[j][i];
                for (var k = 0; k < n + 1; k++) {
                    inputMatrix[j][k] = inputMatrix[j][k] - baseInner * inputMatrix[i][k];
                }
            }
        }

    }


    // 生成拟合方程
    for (var i = 0; i < n; i++) {
        if (inputMatrix[i][n] > 0) {
            returnResult.push('+');
        }
        returnResult.push((inputMatrix[i][n] + '*x^' + (n - 1 - i)));
    }
    // $('#function').text('y=-(' + returnResult.join('') + ')');
    console.log('y=-(' + returnResult.join('') + ')');
}

data = [{x: 1, y: 1},{x: 2, y: 2},{x: 3, y: 3},{x: 4, y: 4},{x: 5, y: 5},{x: 6, y: 6},{x: 7, y: 7},{x: 8, y: 8},{x: 9, y: 6},{x: 10, y: 8},{x: 11, y: 7},{x: 12, y: 6},{x: 13, y: 5},{x: 14, y: 4},{x: 15, y: 3},{x: 16, y: 2},{x: 17, y: 1},{x: 18, y: 3},{x: 19, y: 1},{x: 20, y: 2},{x: 21, y: 3},{x: 22, y: 4},{x: 23, y: 5},{x: 24, y: 6},{x: 25, y: 7},{x: 26, y: 8}];


polyfit(data);