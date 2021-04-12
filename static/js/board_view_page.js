// Load in the catan board SVG into the div
$('#catan-board-container').load('static/img/catan_board.svg', () => {
    // Apply the right classes to the <g>s in the loaded SVG
    let numberTokenIndex = 0;
    for (let terrainIndex = 0; terrainIndex < terrainHexes.length; terrainIndex++) {
        let g = $(`#terrain-hex-${terrainIndex}`);
        let classToAdd = svgClassConversions[terrainHexes[terrainIndex]];

        g.addClass(classToAdd);


        if (classToAdd !== 'desert') {
            let text = g.children('text').first();
            let numberToken = numberTokens[numberTokenIndex++];
            text.html(numberToken);
        }
    }
});