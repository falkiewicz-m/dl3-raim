$("#id_kod").change(function ()
		{
			var kodpocztowy = $(this).val();
			$.ajax(
			{
				url: '/ajax/weryfikacja/',
				data: {'kodpocztowy': kodpocztowy},
				dataType: 'json',
				success: function(data)
				{
					var response = "";
					if(data.is_valid == 'falszywy' || data.length >6)
					{
						response = "Niepoprawny format kodu pocztowego.";
						document.getElementById("weryfikacja").style.color = "red";
						document.getElementById("id_kod").style.border = "2px solid red";
					}
					else
					{
						response = "Adres poprawny.";
						document.getElementById("weryfikacja").style.color = "green";
						document.getElementById("id_kod").style.border = "2px solid green";
					}
					document.getElementById("weryfikacja").innerHTML = response;
				},
				error: function()
				{
					console.log("Coś poszło nie tak");
				}
			});
		});