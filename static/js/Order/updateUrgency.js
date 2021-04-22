const LABOUR_INTENSITY_LOW_AS_DAYS = 3;
const LABOUR_INTENSITY_MEDIUM_AS_DAYS = 6;
const LABOUR_INTENSITY_HIGH_AS_DAYS = 9;
const LABOUR_INTENSITY_VERY_HIGH_AS_DAYS = 14;

const LABOUR_INTENSITY_LOW = 'Low';
const LABOUR_INTENSITY_MEDIUM = 'Medium';
const LABOUR_INTENSITY_HIGH = 'High';
const LABOUR_INTENSITY_VERY_HIGH = 'Very high';

const LABOUR_INTENSITY_SELECT_ID = 'id_labour_intensity';
const TARGET_COMPLETION_DATE_INPUT_ID = 'id_target_completion_date';
const URGENCY_SELECT_ID = 'id_urgency';

let targetCompletionDateValue, urgencyValue = null;
let labourIntensityValue = $(`#${LABOUR_INTENSITY_SELECT_ID}`).val();
let labourIntensityAsDays;

let currentDateTime = moment();

function getLabourIntensityAsDays() {
    labourIntensityValue = $(`#${LABOUR_INTENSITY_SELECT_ID}`).val();
    switch (labourIntensityValue) {
        case LABOUR_INTENSITY_LOW:
            return LABOUR_INTENSITY_LOW_AS_DAYS;
        case LABOUR_INTENSITY_MEDIUM:
            return LABOUR_INTENSITY_MEDIUM_AS_DAYS;
        case LABOUR_INTENSITY_HIGH:
            return LABOUR_INTENSITY_HIGH_AS_DAYS;
        case LABOUR_INTENSITY_VERY_HIGH:
            return LABOUR_INTENSITY_VERY_HIGH_AS_DAYS;
    }
}

function getDateDiffAsHours() {
    let sum = moment(currentDateTime).add(getLabourIntensityAsDays(), 'days');
    let result = moment.duration(targetCompletionDateValue.diff(sum)).asHours();
    return result;
}

function updateUrgencyValue() {
    let restOfDays = getDateDiffAsHours() / 24;
    const selectElem = $(`#${URGENCY_SELECT_ID}`);

    selectElem.prop('readonly', true);
    selectElem.prop('disabled', true);

    if (restOfDays > 5) {
        selectElem.find('option[value="Low"').prop('selected', true);
    } else if ((restOfDays > 3) && (restOfDays <= 5)) {
        selectElem.find('option[value="Medium"').prop('selected', true);
    } else if ((restOfDays > 1.5) && (restOfDays <= 3)) {
        selectElem.find('option[value="High"').prop('selected', true);
    } else if ((restOfDays >= 0) && (restOfDays <= 1.5)) {
        selectElem.find('option[value="Very high"').prop('selected', true);

    } else {
        selectElem.find('option').prop('selected', false);
        // $('#select option').prop('selected', false);
        if (selectElem.find('option[value="Error"').length === 0) {
            selectElem.prepend('<option value="Error">Error</option>');
        }
        selectElem.find('option[value="Error"').prop('selected', true);
    }

    // selectElem.prop('disabled', true);
};

$(`#add_order_button`).on('click', function() {
    const selectElem = $(`#${URGENCY_SELECT_ID}`);
    selectElem.prop('disabled', false);
});

$(`#${TARGET_COMPLETION_DATE_INPUT_ID}`).on('input', function(ev) {
    targetCompletionDateValue = moment(this.value);
    updateUrgencyValue();
});

$(`#${LABOUR_INTENSITY_SELECT_ID}`).on('change', function(ev) {
    updateUrgencyValue();
});
