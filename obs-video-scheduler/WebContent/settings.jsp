<%@page import="util.Config"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script
	src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<title>Settings</title>
</head>
<body>
	<div class="container">
		<form action="/UpdateConfig" method="post">
			<div class="panel panel-default">
				<div class="panel-heading">Settings</div>
				<div class="panel-body">
					<div class="panel panel-default">
						<div class="panel-heading">OBS</div>
						<div class="panel-body">
							<div class="form-group">
								<label for="obs-host">OBS host</label> <br> <input
									id="obs-host" type="text" name="obs-host"
									value=<%out.println(Config.getOBSHost());%> />
							</div>

							<div class="form-group">
								<label for="obs-video-dir">Video directory on OBS host</label> <br>
								<input id="obs-video-dir" type="text" name="obs-video-dir"
									value=<%out.println(Config.getOBSVideoDir());%> />
							</div>
						</div>
					</div>
					<div class="panel panel-default">
						<div class="panel-heading">Scheduler</div>
						<div class="panel-body">
							<div class="form-group">
								<label for="server-video-dir">Video directory on the
									server</label> <br> <input id="server-video-dir" type="text"
									name="server-video-dir"
									value=<%out.println(Config.getServerVideoDir());%> />
							</div>
							<div class="form-group">
								<label for="scene-name">Scene name</label> <br> <input
									id="scene-name" type="text" name="scene-name"
									value="<%out.println(Config.getSceneName());%>" />
							</div>
							<div class="form-group">
								<label for="source-name">Source name</label> <br> <input
									id="source-name" type="text" name="source-name"
									value="<%out.println(Config.getSourceName());%>" />
							</div>
							<%
								int layer = Config.getSourceLayer();
							%>
							<div class="form-group">
								<label for="source-layer">Source layer</label> <br> 
								<select class="custom-select" id="source-layer" name="source-layer">
									<option <%out.println(layer == 0 ? "selected" : ""); %>value="0">0</option>
  									<option <%out.println(layer == 1 ? "selected" : ""); %>value="1">1</option>
  									<option <%out.println(layer == 2 ? "selected" : ""); %>value="2">2</option>
									<option <%out.println(layer == 3 ? "selected" : ""); %>value="3">3</option>
  									<option <%out.println(layer == 4 ? "selected" : ""); %>value="4">4</option>
  									<option <%out.println(layer == 5 ? "selected" : ""); %>value="5">5</option>
								</select>
							</div>
						</div>
					</div>
				</div>
				<button type="submit" class="btn btn-primary">Update</button>
				<a role="button" class="btn btn-secondary" href="/">Back</a>
			</div>
		</form>
	</div>
</body>
</html>