import '../styles/styles.scss';


/*
 * Is triggered when selecting a specific Subject from Search results
 * Updates all UI Elements
 */
function selectSubjectSearchItem(subjectSelectionItem) {
    document.querySelector('#subject-search-mask').value = subjectSelectionItem.getAttribute('data-name');
    document.querySelector('#storage-subject-id').value = subjectSelectionItem.getAttribute('data-id');
    document.querySelector('#button-next-step').classList.remove('disabled');

    document.querySelectorAll('#subject-selection-group, #subject-selection-loader').forEach(function(item) {
        item.classList.add('visually-hidden');
    });
}


/*
 * Show Search Results and handle Loader Icon during request-time
 */
function showSubjectSearchResults() {
    const subjectSelectionLoader = document.querySelector('#subject-selection-loader');

    subjectSelectionLoader.classList.remove('visually-hidden');

    setTimeout(function() {
        subjectSelectionLoader.classList.add('visually-hidden');
        document.querySelector('#subject-selection-group').classList.remove('visually-hidden');
    }, 1000);
}





/*
 * EventListener for Triggering Search by Type
 */
document.querySelector('#subject-search-mask').addEventListener('input', function() {

    if(this.value.length < 3) {
        return;
    }

    showSubjectSearchResults();
});


/*
 * EventListeners for Selecting Subject Item
 */
document.querySelectorAll('.subject-selection-item').forEach(function(item) {
    item.addEventListener('click', function() {
        selectSubjectSearchItem(item);
    });
});
