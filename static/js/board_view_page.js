const findGetParameter = (parameterName) => {
    let result = null,
        tmp = [];
    let items = location.search.substr(1).split("&");
    for (let index = 0; index < items.length; index++) {
        tmp = items[index].split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    }
    return result;
}

const terrainHexes = findGetParameter('hexes').split(',');
const numberTokens = findGetParameter('numbers').split(',');
const score = findGetParameter('score');
const color = findGetParameter('color')
let svgClassConversions;

$.getJSON("static/generated/svg_class_conversions.json", (json) => {
    svgClassConversions = json;

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

    $('#balance-score-display-value').html(parseFloat(score).toFixed(4))
    $('#balance-score-display-inner').css({
        'background-color': `#${color}`,
        'width': `${parseFloat(score) * 100}%`
    })
});
