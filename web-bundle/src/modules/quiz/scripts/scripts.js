import '../styles/styles.scss';


/**
 * Select correct AnswerElement and handle Formchanges
 * @param {*} element 
 */
const handleAnswerSelection = (element) => {
    document.querySelectorAll('.quiz__answer').forEach((item) => {
        item.classList.remove('quiz__answer--selected');
    });

    document.querySelector(
        `#answer-selection-${element.getAttribute('data-key')}`
    ).checked = true;

    element.classList.add('quiz__answer--selected');

    enableSubmitButton();
}


/**
 * Remove Disabled Class From Evaluate Button
 */
const enableSubmitButton = () => {
    document
        .querySelector('#button-evaluate')
        .classList
        .remove('disabled');
}



/**
 * Eventlistener to trigger Selection of Answer
 */
document.querySelectorAll('.quiz__answer:not(.quiz__answer--validated)').forEach((element) => {
    element.addEventListener('click', () => {
        handleAnswerSelection(element);
    });
});