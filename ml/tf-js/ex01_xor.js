const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

const dimIn = 2
const dimOut = 1
const numNeurons1 = 20
const numNeurons2 = 5
const learningRate = 0.01
const numIterations = 100
const batchSize = 20
const W1 = tf.variable(tf.randomNormal([dimIn, numNeurons1]))
const b1 = tf.variable(tf.zeros([numNeurons1]))
const W2 = tf.variable(tf.randomNormal([numNeurons1, numNeurons2]))
const b2 = tf.variable(tf.zeros([numNeurons2]))
const W3 = tf.variable(tf.randomNormal([numNeurons2, dimOut]))
const b3 = tf.variable(tf.zeros([dimOut]))
const optimizer = tf.train.adam(learningRate)
const eps = tf.scalar(1e-7)
const one = tf.scalar(1)

/*
* 모델은 주어진 입력에 대한 예측을 출력합니다.
*/
function predict(input) {
    return tf.tidy(() => {
        const hidden1 = input
            .matMul(W1)
            .add(b1)
            .relu()
        const hidden2 = hidden1
            .matMul(W2)
            .add(b2)
            .relu()
        const out = hidden2
            .matMul(W3)
            .add(b3)
            .sigmoid()
        return out.as1D()
    })
}

/*
* 모델 예측과 실제 라벨의 오차를 구하는 손실 함수
*/
function loss(prediction, actual) {
    // 머신러닝 모델 학습을 위해 올바른 오류 측정 방법을 사용해야 합니다.
    return tf.tidy(() => {
        return tf
            .add(
                actual.mul(prediction.add(eps).log()),
                one.sub(actual).mul(
                    one
                       .sub(prediction)
                       .add(eps)
                       .log()
                )
            )
            .mean()
            .neg()
            .asScalar()
    })
}

/*
* 비동기적으로 모델을 학습시키는 함수
*/
async function train(numIterations, done) {
    for (let iter = 0; iter < numIterations; iter++) {
        let xs, ys, cost
        [xs, ys] = getNRandomSamples(batchSize)
        cost = tf.tidy(() => {
            cost = optimizer.minimize(() => {
                const pred = predict(tf.tensor2d(xs))
                const pretfoss = loss(pred, tf.tensor1d(ys))
                return pretfoss
            }, true)
            return cost
        })
        if (iter % 10 == 0) {
            await cost
                .data()
                .then(data => console.log(`Iteration: " ${iter} "Loss: " ${data}`))
        }
        await tf.nextFrame()
    }
    done()
}

/*
* 모델의 정확도를 계산하는 함수
*/
function test(xs, ys) {
    tf.tidy(() => {
        const predictedYs = xs.map(x =>
            Math.round(predict(tf.tensor2d(x, [1, 2])).dataSync())
        )
        let predicted = 0
        for (let i = 0; i < xs.length; i++) {
            if (ys[i] == predictedYs[i]) {
                predicted++
            }
        }
        console.log(`Num correctly predicted: ${predicted} of ${xs.length}`)
        console.log(`Accuracy: ${predicted / xs.length}`)
    })
}

/*
* 랜덤 샘플과 상응하는 라벨을 반환하는 함수
*/
function getRandomSample() {
    let x
    x = [Math.random() * 2 - 1, Math.random() * 2 - 1]
    let y
    if ((x[0] > 0 && x[1] > 0) || (x[0] < 0 && x[1] < 0)) {
        y = 0
    } else {
        y = 1
    }
    return [x, y]
}

/*
* 랜덤 샘플을 반환하는 함수
*/
function getNRandomSamples(n) {
    let xs = []
    let ys = []
    for (let iter = 0; iter < n; iter++) {
        let x, y
        [x, y] = getRandomSample()
        xs.push(x)
        ys.push(y)
    }
    return [xs, ys]
}

let testX, testY
[testX, testY] = getNRandomSamples(100)

// 학습 전 테스트
console.log("Before training: ")
test(testX, testY)

console.log("=============")
console.log(`Training ${numIterations} epochs...`)

// 학습 직후 테스트
train(numIterations, () => {
    console.log("=============")
    console.log("After training:")
    test(testX, testY)
})