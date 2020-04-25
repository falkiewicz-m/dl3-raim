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
						response = "Niepoprawny format adresu pocztowego.";
						document.getElementById("weryfikacja").style.color = "red";
					}
					else
					{
						response = "Adres poprawny.";
						document.getElementById("weryfikacja").style.color = "green";
					}
					document.getElementById("weryfikacja").innerHTML = response;
				},
				error: function()
				{
					console.log("Coś poszło nie tak");
				}
			});
		});