let scheduledTranscript = null;

function playTranscript(transcript, index) {
    const currentTime = player.getCurrentTime();
    let {audio, dur, ...rest} = transcript[index];

    console.log(audio);
    console.log(player.getCurrentTime(), transcript[index].start)

    if(index + 1 < transcript.length) {
        const start = parseFloat(transcript[index + 1].start);

        scheduledTranscript = setTimeout(playTranscript, (start - currentTime) * 1000, transcript, index + 1)
    }
}
