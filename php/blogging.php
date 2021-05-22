<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

    <title>scintilla</title>
</head>
<style>
    form{
        background-color: blanchedalmond;
    }
    .label{
        font-weight: bolder;
        font-family: 'open sans';
        font-size: 2rem;
    }
    textarea{
        width: 100%;
        resize:vertical;
    }
    h2{
        display:flex;
        text-align:center;
        justify-content:center;
        margin: 30px;
        background:rgb(183, 183, 243);
        color: rgb(82, 30, 40);
        
    }
    table{
        background-color: rgb(170, 235, 235);
    }
    tr{
        background-color: rgb(220, 170, 50);
        
    }
    th{
        padding:0px 15px;
        background-color: rgb(220, 170, 50);
        font-size:2.5rem;
    }
    td{
        padding:0px 10px;
        font-size:1.5rem;
    }

</style>

<body>
    <!---------------------------navigation bar--------------------------->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Scintilla</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="index.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Destinations</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="place.html">Tour</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Services
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About us</a>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>

    <!----------------------------carousel-------------------------->
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="blog.jpg" class="d-block w-100" alt="...">
            </div>

        </div>
    </div>
    <!---------------------------heading--------------------------->
    <section class="py-0 text-center container" id="top">
        <div class="row py-lg-5">
            <div class="col-lg-6 col-md-8 mx-auto my-0">
                <h1 class="fw-bold" style="font-family: 'dm-derif-display';text-align: center; font-size: 5rem;">
                 BLOG</h1>
                <hr>
                <h2 class="fw-bold"
                    style="font-family: 'dm-derif-display';text-align: center; font-size: 3rem; color: rgb(150, 37, 37);">
                    Of TRAVAHOLIC.</h2>
                <p style="float: right;">
                    <hr>
                    <button class="btn btn-outline-danger" style="float: right;"> <a href="#foot">Top to
                            back</a></button>
                </p>
            </div>
        </div>
    </section>
    <!---------------------------content--------------------------->
    <table class="container">
        <tr>
        <th>Name</th>
        <th>Review</th>
        <th>Date</th>
        </tr>
        <?php
        $conn = mysqli_connect("localhost", "root", "", "blog");
        // Check connection
        if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
        }
        $sql = "SELECT username, comment , date FROM blogging";
        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["username"]. "</td><td>" . $row["comment"] . "</td><td>"
        . $row["date"]. "</td></tr>";
        }
        echo "</table>";
        } else { echo "0 results"; }
        $conn->close();
        ?>
        </table>
        <div class="container-fluid my-5 forum">
        <h2>Share your experiences and reviews here...</h2>
        <form method="post" action="connect.php" class="container">
        <span class="label">Username : </span><input type="text" name="username"><br><br>
       <div class="label">Review:</div><textarea name="comment"></textarea><br><br>
        <span class="label">Date:</span><input type="date" name="date"><br><br>
        <input type="submit" value="Submit">
        </form>
        </div>
    <!---------------------------upper footer--------------------------->
    <footer class="text-muted py-5 my-3">
        <div class="container">
            <p class="float-end mb-1">
                <a href="#">Back to top</a>
            </p>

    </footer>
    <!---------------------------lower foooter--------------------------->
    <footer class="my-0 pt-5 text-muted text-center text-small  bg-dark" id="foot">
        <p class="mb-1">&copy; 2021-2021 Scintilla</p>
        <ul class="list-inline">
            <li class="list-inline-item"><a href="#">Privacy</a></li>
            <li class="list-inline-item"><a href="#">Terms</a></li>
            <li class="list-inline-item"><a href="#">Support</a></li>
        </ul>
    </footer>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
        crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" crossorigin="anonymous"></script>
    -->
</body>

</html>