import random

list_dogs_img_url = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn3ROq4I-EO9H3y9GkXMpV7fzuuRVHQOK2_w&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQToZnbhjpxId9f23qr_xK181cyk260fs-xUJK7scBOd6Ixy6lFM7xv7QD-pDP-yYIVoec&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVKJyXKAuML8W6T1i3Dy5qY7_89ARlgIkPw4uEktAEvjC3ziIbyt7_-ip-neYaaMkCUa0&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTagu1pUOeEq5AyJO_NnGa0Qs5IuLIH9RVL_A&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrdO-MQT0KsZ87cX388JnkBNlgGj9x_zNGoQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz3yRDbmoq2WQ9LdNIfVrxyus6fwlsvBa5uLkgpdU5QRb20bxwNRgguL6XeQWzuOcxy7Q&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI88aJr2cDJo_IstAMJ8iXRzbRsmZG6Cp5WA&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtLab1-iE1T4tXSm8CZ7rq7YwSDCNnGC4OkQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyPqWfuIUqnNMF_n8OpOoHloX69oTc9CuKj9tfVhocgc6uPEtX35szolAv1fM7NitCiSo&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBnniVnnvoQVjwzf-LjU2TNACgp4lxjSUSOw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIYSKzAAQCpFngKw1RFvzTqgf_d01yJV8WMg&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWpWl3fC6IdEZKiEsLVZxEOjX42Dg_OXSyhg&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT_EUI5Wk1M6BrW7DTFdYV1PfExqEUQq_4bQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROkWJg2TG_1BjooGzCOcyaq-12LqghxPJgvA_yKD3VCWcCxcDeRPpLtszfckeukrtdNUM&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKmG8WybXmH-yZ5W5aNi1clsI57IH4MYlf-w&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsfQld9divAavTCXlSfICKU61tKHlnS79Ukw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9iTZCa_luK7GZ2Te_uhdQTnTKfMbCn2Fz6g&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaTVvanPQg2KJNbMsxK1Ts8ck0b_p8-vgayA&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKpt49iD3SrsVJ5ZV_YmTlRDdu94GWADQBUg&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSv1ho6jYlopftZrLYJ_05CcJvtE5rD5Tu5w&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDY_vTwSGySL77iOLf3hVcKYUgTK1AyCkT32PGVKtKWxb142U7G_PtOAcY2PlXL56e6r0&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqbT7a-GMLpt5mcMk-fUjsHu1aGXivlszRng&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDrLVt1B-8aXmxwn6NlxRoLj71dHLYToQKpItwdk33t6d13U7nBCDBPrv_CloeRcT8dyg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNa_PxzHImcp4tefF-YvH_6dyt5vF34vnXxw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP2Yie-FCiX55xWSZW3-lrLYnW1eM4aMhRHQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8RH95YdEzEO-cWstPE-7thZIc4wKe9KcJ0A&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyz2qFBIAzJ7B34lM69BnpK-jwaZneeyYFQppur4jC6-7wqe9kmMdi5gE37_cP9ye0vio&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgqXOcPoI-f-vem2S3wxDCrAuNG0mm0j1chuTfl508doy0gNpH81b421es4sjmKW4rrLw&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbLD04VXdFLn7lp71l1feXmf9NiuDezuwRUoy3HdNlLaYMJuPxstNv-yNydAaRAfyA7hM&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1t73bpzyXPJV37qjmGk_uSISuuzoqAss5lA&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnxsg6N2G8YClBkA-32wiv5Z2AeowboMNzZYP68H-0sXMhj6L9rJLTMm34rmN37HDs9jg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgAhfyPlp40Ky_oaARcfjLxMZkqfQ2zkNRY_YKXZd5RuvnMsk8Ba-cEo-uTCyStx9MRsk&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxA5Uwdh4CAS8g8LgM1Q1Gy3qDUiyVmOLpog&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp0vLylQxOkzQpYsImNP5BUnM5SztAwRR3xw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRb1FkmUEk8lcD_bCY2gwCpITj9w1OIAwNrUQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ27c_qUFV1Hus5twxW2w5npJPFkSOcpU5DNw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ27c_qUFV1Hus5twxW2w5npJPFkSOcpU5DNw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJVV0AF0RUpIyrpIxq86ZeEQ9J4D68HX5Vlw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT196_GneZ5N51U5HtmuvVAZPw3wlw36LR-Vg&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmxZ-GbfPszeU8q5tHODKIxW1Clij-fnvkYQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQjSyDpfU2VuyPdBrZj27AKIGPeSyVIcFORZH11nPCeffJIt2IQlPyRpkcnkNYjba7uq4&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWiEi0gMiy79XBFw_HSxKFgqdCtd_yHMBKfvtYL5Jl_6lYqtajehbtzEqzIkVbvLE9W4w&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-Qktpm5SOxgHkdtSl4vvS8tYY7UtVWQn8Ds3a8lCQLJ7KlbqgucN_DlX5HgXaevHv34o&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-ixVbFAqR_QE3CODwb3rVxZczkiar5Ik71w&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu97tXz6qcz6cscCaKupk7blM3c9cM33fT4VC775mI-UfFgBOHic1M1rMzpBfQdAYXJz8&usqp=CAU'
]

async def dog(client, message):
    await message.delete()
    await message.reply_photo(random.choice(list_dogs_img_url))