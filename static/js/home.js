let balancedData = null, unbalancedData;


$.getJSON("static/generated/balanced.json", (json) => {
    balancedData = json;
});

$.getJSON("static/generated/unbalanced.json", (json) => {
    unbalancedData = json;
});

/*
// Handles the press of one of the two <button>s in #home-button-container by doing the following:
// 1) Makes the pressed button show a loader by adding the is-loading class
// 2) Disables the other button
// 3) Redirects accordingly
//
// isBalanced: a boolean, where true indicates that the button for generating balanced boards has been pressed and
//             false indicates that the button for generating unbalanced boards has been pressed
 */
function handleHomeButtonPress(isBalanced) {
    if (balancedData === null || unbalancedData === null)
        return;

    if (typeof isBalanced !== 'boolean') {
        throw 'Parameter isBalanced is not a boolean!';
    }

    let pressedButton = isBalanced ? $('#balanced-button') : $('#unbalanced-button'),
        otherButton = isBalanced ? $('#unbalanced-button') : $('#balanced-button');

    pressedButton.addClass('is-loading');
    otherButton.attr('disabled', 'true');

    let usedData = isBalanced ? balancedData : unbalancedData;

    let selectedBoardIndex = Math.floor(Math.random() * usedData.num_boards);
    let selectedBoardData = usedData.boards[selectedBoardIndex];

    // Redirect according to board data
    window.location.href = `/view-board/?hexes=${selectedBoardData.hexes}&numbers=${selectedBoardData.hexes}&score=${selectedBoardData.score}&color=${selectedBoardData.color}`
}