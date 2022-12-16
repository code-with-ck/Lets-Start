
let a = document.getElementById("dynemic-text")


let phrases = ["SoftWare Engineer...........", "Mentor..........", "Human being........"]

let phraseIndex = 0
let latterIndex = 0

function printLatter(phrase) {
    if (latterIndex === phrase.length) {
        cleareLatter()
    } else if (latterIndex < phrase.length) {
        a.textContent += phrase[latterIndex]
        latterIndex += 1
        setTimeout(function () {
            printLatter(phrases[phraseIndex])

        }, 300);
    }
}


function cleareLatter() {
    if (latterIndex == -1) {
        phraseIndex = (phraseIndex + 1) % phrases.length;
        latterIndex = 0;
        printLatter(phrases[phraseIndex])


    }
    else if (latterIndex > -1) {
        updateLatter = ""
        for (let index = 0; index < latterIndex; index++) {
            updateLatter += phrases[phraseIndex][index]
        }
        a.textContent = updateLatter
        latterIndex--;
        setTimeout(cleareLatter, 200);
    }
}


printLatter(phrases[phraseIndex])

