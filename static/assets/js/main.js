function submitForm() {
    document.getElementById("taskForm").submit();
}

function submitOnEnter(event) {
    if (event.key === 'Enter') {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById("newTaskForm").submit();
    }
}

$('.datepicker').datepicker();


//function submitOnEnter(event) {
//    if (event.key === 'Enter') {
//        event.preventDefault();  // Prevent the default form submission
//        const taskDescription = document.getElementById("task_description").value.trim();
//
//        if (taskDescription !== '') {
//            document.getElementById("newTaskForm").submit();
//        } else {
//            // Handle empty task description, e.g., display an alert
//            alert('Task description cannot be empty.');
//        }
//    }
//}