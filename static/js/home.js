/*
// Handles the press of one of the two <button>s in #home-button-container by doing the following:
// 1) Makes the pressed button show a loader by adding the is-loading class
// 2) Disables the other button
// 3) Sends a POST request to the backend, requesting the creation of a balanced or unbalanced board
// 4) Waits for the board to generate and for the backend to redirect the page to the board viewing page
//
// isBalanced: a boolean, where true indicates that the button for generating balanced boards has been pressed and
//             false indicated that the button for generating unbalanced boards has been pressed
 */
function handleHomeButtonPress(isBalanced) {
    if (typeof isBalanced !== 'boolean') {
        throw 'Parameter isBalanced is not a boolean!';
    }

    let pressedButton = isBalanced ? $('#balanced-button') : $('#unbalanced-button'),
        otherButton = isBalanced ? $('#unbalanced-button') : $('#balanced-button');

    pressedButton.addClass('is-loading');
    otherButton.attr('disabled', 'true');

    $.ajax({
        type: 'POST',
        url: '/generate-board',
        data: JSON.stringify({'isBalanced': isBalanced}),
        dataType: 'json',
        contentType: 'application/json',
        async: true,
        success: (response) => {
            // Redirect to the returned URL with the board's data parameterized
            window.location.href = response.redirect_url;
        }, error: () => {
            pressedButton.removeClass('is-loading');
            otherButton.attr('disabled', 'false');
        }
    });
}