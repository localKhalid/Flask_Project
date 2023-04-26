<!DOCTYPE html>
<html>
<head>
    <title>Bug Form</title>
    <!-- Include Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-5">
        <h1>Submit Form</h1>
        <form method="post" action="/handle_information">
            <div class="form-group">
                <label for="bug">Name</label>
                <input type="text" class="form-control" id="bug" name="bug" placeholder="What is the Bug?*" required>
            </div>
            <div class="form-group">
                <label for="priority">Priority</label>
                <select class="form-control" id="priority" name="priority" required>
                    <option value="">Select Priority*</option>
                    <option value="high_priority">High Priority</option>
                    <option value="medium_priority">Medium Priority</option>
                    <option value="low_priority">Low Priority</option>
                </select>
            </div>
            <div class="form-group">
                <label for="additional_info">Description</label>
                <textarea class="form-control" id="additional_info" name="additional_info" placeholder="Additional Information (Suggested)"></textarea>
            </div>
            <input type="submit" class="btn btn-primary" value="Submit">
        </form>
    </div>

    <!-- Include Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>
