#Decompiled by Makky Gans
#Kalo Mau Decrypt Silahkan Tapi Izin Dulu Asw
#Jangan Main Recode Ae 
#Kencing Aja Belum Lurus_-
#Recode Tanpa Izin = DPR
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJztfQl4HNlZ4KuWWlK37sOS5bNsj2XZM7pal+UZ2WNb42PGV9r2yOOJaUpdJamkvtxVbUsTOQmZbL6wy5JMmCMbJhcbAlmyw36B5QrwJewCgSUJ8BHOAImzIbBsFvYgC2xI9v//914d3dWtlmfsmZDx8frVq3dV1Xv//f8vycSfMPx/GP5boVrGdPinsBRjV528wq4qMh9iV0MyX8Ou1sh8LbtaK/NhdjUs83Xsap3M17Or9TLfwK42yHyEXY3IfJRdjcp8I7vaKPNN7GoT5UMs1czSLexqC1NW23y3ZzM7WK3RypajLP9FpiiKwdgSVKlhTytMycTYFbcB9e1t0Ky4DWp5A4Vdwdphlmpn6Q52tYMpeF2Hw6U72dVOphhdzFCoNvwsbWJ6Pb9oYkud7Gl4id3M6GZLPczYzG/ARS/D21vY0lasocNriMA9RdFPsAUFqye2Mb2JvR1ab2d6M2V2MDG1FupGb2VXdzK9je6pTG9n2i62APndmGp7KL2P0r1U3kfpPkr7Kd1P6QFK76f0AUoHKB2kdIjSYUpHKI0xHV7EKNPh8ceY3kUTGGf6JspMML2bMpNM76HMQaZvpswU03spc4jpWyjzINO3UuYhpm+jzDTTt1PmMNN3UOYI03dS5mGmq5Q5yvRdlDnG9N2UOc70PZSZYfp9lHmE6Xspc4LpfZQ5yfR9lDnF9H7KnGb6fso8yvQDlHmM6fdT5gzTH6DMWaYPUOYc0wcpc57pQ5S5wPRhyryB6SOUiTM9RpmLTB+lzCWmj1HmMtPHKfM40ycoM8v0ScpcYfpByjzB9CnKXGX6Ico8yfQHKfNGpj9EmWtMn6bM9zD9MGUSTD9Cme9l+sOU0Zh+lDJzTD9GmSTTj1NGZ4bB9Bn2dtjP88xYYPojbDnE8t+qMcZxJSoZ2hoX+08CLDC/DX/O9SuQtaOQXFrMG5p+IZtNWd1wmTNzMdXMWLaWSqlpI7moZcynDGtT8a28cb1gWLbFO2qF5Hg2kzGStpnNPJLPZ/P8Rj0kx/LZm5aRtwEGsYI9f9BugExaW0nYZtowsZqFE7kMdQaOLhgZ25qFy/M5I68NTQ0eHFb7j2b0fNbUH1SpUD1rZsyh0YnB2GAsNj42NDIyNTgyGntQvfygaur71Qt5mFh2KDY4Ehsci42qjxt5C2Y1BJcjE0kJG3Hc4zg2PjW8nZOnbNiIsNdD9MoAHlzsD8Gtc1YbpFufHHlwaiT95K5r6qWCXcj11+DT4f2sZWPeWrXoAY0V0+7H/t3Ewmr6gl0HP8tGqqDle7G0lmYRVpI4E6xSI2eEycpDbI3m1TNzbZjdUpgzuzUOlsR1Dc0Whl4KIwjFO9cB/tH0a2j62H104U1dL5388lNvP9KPs4hjQvOxbD1bsG1EFDfzpm1Qbj5VsBbpafALUZGVMowcvQ8b+3uKUqP0GbHukpbSAP5CYQM9YrvSpjQr1j58Kn1hIJszMuqibecODQ2twuCFOWMwmU0PJYfOasvLq7GJqVHrMehHpXceS99+/p3l/kV9dd5eUgFLVPmHqk6mb7/wrtvPf7zcvy/9/DN/8rE/+Rj8lK30wru8w/LsKGR/0fvPGW5ATagDA4mBAafNc8/efu6jt5974fazP3D72bfefvbdt5/9uCeDhTBbqvZurIaZF1TfmLJzJ5OgEQZoqISsCX08g/+efZG6/whlYIT3UuanacC3in/Pfej2c/9WpZ+PwXDBT/gJ7z/nAQdUlT+k+4Tvpl7eD4OoNBD8e5YGomt6uvdRQlXfr8ohYOemzUI6WsWnL/6sv/IT086f2y/+mHvxK5+Mui+EN/Utnsm0fNWvtX8veGb4jHxFB5wnPlqwF7N59x2MpA+J3ERapa2kXtCWDfWklrE8K8bzB7qtPMRJ0z5VmAsaAl7m1ichxX1swUZeMO3FwhztY2cXb33S/TzrjwXow9aStn8sMRgNlbW15YKhm3Y2H5t4eCGtmSkcj0bxPR92r6qe0d73an/JwH/vV6NR8S6fPHBNvWimtMVlLaOeyS4AVFSPLhcy6oyWN9WjuWX1hJY05rLZZW+LGV7ZzHC0mAasqB5d0PLqJVPXltXji0ZyOZc1M3aUkJ4PxZzgSA8wBhDRCzXsFsDmYcQ4M9f6EdsApQx4puekDycColuqRbKZsEy3wDJ1hGUQWwzCa+eZQSczqFr3QaZZIlAAn9fkEjqT1XQzsyA/lIujwhJHxSOYNGLShEkz4hvCQmHCTra5TJgoW4qJCEGby32SvGChVsBCDfDfpGrNhNVHR9Lnsrb6eCGVsSK8JJbGK3plOHCdfGW/Ch3z16FzDLy6BSkA/gqfDuErtDk2ns28EKoF/AmTnA8RD/KpELABvsaAfU+e0ultdkEGr4BY4lwGYvsGttSALARehpgdoY5X25Fmg69BjAUOpLJau5EtNdEon0DWSI9iV82c7gNGx26hNq0s0UaZdqY3IhfyNFSGT4xFHciMPLQWkhct7CHMdfKPDrkuzN0ClrCVrdWw5TqWnwutDirApuAiASalBxr3AAPRc6uWmY3IRAAHMQHMA7ANE1AH+p8AxgFYhgngFoBPoJ+t8LMNWYMJ4AqAH5iAXqDNBHAEwAtMABsADMDErTCzN7GlbmQC8G3UsbU6ZLzWODOHF5tpfvVsLYw3gKRcq0dOYYI4qj6cud2LjBlMHtiFNVzAyq0GZm9lS9vYGrzq7dRzRH7PfvqeUbYGz76DrUWQpeilwaBgJ6cPD+Brhl5V5C5ElR76srvY0m7kNOhCrIjrc7AioPYetnQffavvCRV9K6hxBen0AfmKXwgBbyKpUuBOPH0P8wvR8NMh4FQqVtzrrAbasTHcsbSDkilDy9PCTyEgGbRXbNpPeXNM7hsHir7bGvMQwrff+w5nH589evHyY+rRxy6fU08cPf7IsfPnH1O99az7PQ3v581GJ9JI8Ge0tOHAe4lZytS/oFnWzWxeL62PJLzEROnBeQErETtY25H69VLvBBuP6pr6WDZjLFsmEfGZPAEFeicGYhaifnMwoIUwwNJuGAO6ccNMGhbyUFrOTCwbq9MHD8a0g2NTw6MTI7o2dXByODY3PzWpDcdGdD05MqYn84YO/IyppayEvZozpnPiEWiMaet7kdjO5tOaPf3oxfPngPcBOG4bibSWXDQzRsLUp0ecQsuwkI1JJOHRTMOaHkllk1rKmDYyicsXgUxfzOrTGtAEg/Qp5UjT1oP4PQ27kM8kLCuVAOYoW8jDg0wP35geGRyeiM0fTBpT85NjcyOQHUuOxEaTydjo2OikNqaNxmwV2q/3oMTnibdC7J0c3kbmqfg10MvFByYWhL8AWnYjdiekAa/B3uwtL3oT/KvhW6D++Guhteu+DrrDXxKNNGx3lXktFiIOeC9U7QahkbQ+znk8c4G4GLnU4IF9i20IGU9Y1DeM/GBuMUdj5jTAzBZ1dtNGHKYlcZCEnV02Mtawd3UK2u32iz8kSjyIErG8VaCm1lnPFBbyWm7RP4m0MTSfN42Mbh0RqyIHPGpfwdSt6YWbZrpgaaN93llMm44wIOnQDNZg0cYRBNvRZDJbyNjqKc1SjxnAyblkBjHK+bQ6kJ9XHXDiIHWrp6jDk9qClgJC1Sos9yOWjocdphR4aSNNqwSZRcqkjUyBVtZjxirJF2jJnT7P87UcgmVtBGV57WYCNgCwtfW0amxcjHFcWbTX5/JUy5FtUK+X42eopzheUHeX8gV+KwFvF2jOVerNtBKLdjplE1QwUkbSTuD6pRaUofkX5tKmTdkFXGEparqoWYspc45WUsa4SbcLOR0WNM1n0VjRzQVYQDSoFK9QbeiEBliygEYO06NqOhc32MaKHY9K0JVMZS2+u/CTuyQTfVtjJWnkUDxjxRXZgD5Tf6NDUMFysOklwZbDkXM3+S88Q3y/fDMwZY0W9AqlWhyFQ/EWefspQ9dLyLH4Gfh5BK+XsBSosBqlVWlUOiEXViLwvwmu66EUpQVhpTHURFKDZiUKd5qgvFu5qCAF16R0KXXKJqUDrtrhbhjyzdRTWGmBVmHeKsR/iYzDFxqWZFwDTGi1Fyk5Tv8Cpge0ifQDY7OZGaCnOMmWQGJKULxczgzUGmBZLw0ML22pDuXGdFHPsexX2ZXVG0TARZCeA5q6R9B0QDw0IsUE5Bon65DeaWC9QJ+sEU3XC+STaBh1GoZlw7BsWMcA9QPdA4RcL1BySJkA8TObWYbJt9Dktyklk2+uavL90EUDUotLbdTRceqoHWnVFuygw6Urvb3zGq0ouAZqsItIQSjoRFqmB0hBm3JQczPQd3C7m24TDSdv15bc3oxknLxdX3K71x1tCxVsxTlsw2Q7Jjsw2YmJiskuTHbjM3S5Ar49SAn56R++mhE7WFuYX/CHwFLNALswDyBQXwfc3b8elD7ig8G0dZAaip/DoSfXhfEAZKxk3pwz8lZRT/UEgtJpDWAWbW3gnFMJAtvWiP+RBFC/aAADaZuZVU3VkO2EbjQvYN9W9CKKaSg/ofisiQQm4VGkGvnvC9Yh+n2mPLaTLPw5L00oUaC5jwmBoqwmOn6m+o5PHDs9U9Jx9c0vwhsvbe579A+JSb3f2sN7HTjMqdfJB8eG0yODKtK86ukMp3kQFvcH1IsNAnpNuky/KpAu0bnFlUcH1WNZ2+oNuDU2qJ63F2GBBN4dh9kQ+gm8OzEoBBGEtz13R/Du8KD6yIppCyZatoFa/bR7hiQuQNVCPCaRexxpChcrEU6Iz2CCmCGOMok4ktfxU4x4aRRP5+O4ZOOPYYLYJj6KSYOskDI4RsyZKXOxH4vjZ+W9rH0zflHOBLaWRltL3OIkGcfGsJVKERaSZm/F60uEsGqUXkIoHK00hmoA4XQA+onS72bPvSihIkRhWNKu7KS/7VTm/UuoScr+CTXtVZjASwjRGSkAQqTJ2YeAFkCXwsHvP9KtWro1jVQNlf5XKg1T6UUpi8h8jkrrqNTEd0GlP0el9VT6FkT+VPojVNpApb+OtNhSvRQ1AFYA+BlFnNMFE+G3mqQmArAL5biYInOV+mmhfv6v7KdVyj3woo1fRHn9A1S/neo3O6VdqJJELAh4pMd5eILbXQS3N9PKROme2JW3n/8ZuVlt+pbdfsB1XMvss1UjnbNX4zuZ0GXEKB2ldIzScQL/gSwwdrhg2mqukEqp2byJdHlaA3I1b6HGw6FvpUzrGO5jCUio84lAvEHowqcdKeVlh/LmU08NprUF+Invxcl1eR7v9ovPX5OjkrpODovyLe0G8JvanJEiWi+OTxZ/El8Aoj6TgyNghTldnCkkFmHaXE2HV3NZTn+mNDPj2ci0E4fldiR9X/wSC9B80VA/idcTtOaRoAsDidZU8p8Tg7iH+FWzuCMIuXrxn3bLT5XI43p98jiuGiOqbpKhOM6h6jghx5tWoIWQyPGJ7GgL1OMGwS0QEVuDU3awNagOCeNgk0jqLYS02lILEnhLtAOA2Fv5hoKSKKDcZq79nnKLRK1A/8Am6l2uY9bX5HULXec/zUSvrbK0B/ZPT/kRwsyZ5Wo77isgHbFz2ESzmW54F5y2exRpO9hiJ09lJpUrWLOTaraU1LSpZhfW/PeMam6imt0lNT9ANXuw5hO85maq2VtS8zNUcwvWhBe9ugnFgVhzG9C0pXP9BtXeLmu3ox0B1t5ZUlMlwZoqa55hRPmtPEzVd+MrH0MKGgfcQ0T0fe6A18dCspsF6mYvNIXCK/B/djbT7gzyVrxLCySClgiCBObSOAb/ZvV9jC8R302CXbgzznECs5TwfFk0ZyDEOsxKZGlAtpxG/lg9PSMqDoliJL1EZfWQA0284rjbL/6CK/fLLmYz6qVCZmGhICsPDg5aCBiqE1D4CNf4GxCCXMaEaOCtlbuxkOP09+Cf6Qd+3pkpPJdWogE7pFpTnvpH1qstKjrUb9nRnNfqVbaVHa1M7apHewRlicVdHFLjSLeVGbJMk6qHPJdNZ/PqJSOVy2acbg6pJN9KZ+fMlJHIwdIwyr3f4OYefMUX+/4yw5/JLgO28s0fBm9gXPZHZPVk4MCBDUueur/csNqimQ8adc7M24u6tkroLWDUgHYlgz5QZtCLxnI2pS0WfSwYGGGHoRfE8+5xm6ulf94sdycXTyUX0drngWqaeKe4PoFj7SwmSC4YCByAm3S66e9gPnYAeYX4FUyITyjiDkYdcgUhX1lmgTMJSIv0I31APAABEQKqROQns1xVmOOSKsxeL6VUFuDnC3hN9COJqXo9VD+nT5oE1d+uqEDZd0AJiq2alUio/O+momvkDHhpO/RaG4oqLSGgiVyuwBFYvcReVToHiBwi/CFpxKQJk2YpEAKaBJI2juwcFNd+b1HcQyyQ10YzsSJGul/sqktafsGwRRf7aSsEMOFnCynbVI/lC7YBFHLScPqxYgENgBG/WMgBe1++2VhAM2DSqeoJqlpmgjsCGgL//oQGO1k9nkJQe19AFWDij6YBHAOiHyKYP3TqQjl+HjdyAD8f3ehuJVkz8g8JzpMrcj+WbrZF+NkG9wniltts67PNX2JVss3/MZBt/qCHbb4q2WbJJ7/Nwz3nHD455eGe34H8LZU+7uGeX2Rydz1MpREq/QRKdz0cb5RKPyPV+8jxcs4BdlkRx4svuTLHG9fY+hxvfA4TfIdxHRMDk3lMKjOUuKNLEDRfHASdLSbkLGiFwnUReeQhw7QYLDPFrQhxf1BuDpc8LRXiMFdxIVN7IPTmOCBXZJe4mEoXD444hovnAC0IP09ZH8hdOnxkkxe+GuG7DF9D4XXh6+rP1toRwUMKfrLRy082cUOL5kpcXw1ybmtkpIHMDPbR5p1UuxS5AMsXWMxHdCaGXXUCb9RFVh3A+Cxxvg8n0g0TQdF9j6OiaEbLEbKsQO4Kub46smJ4VgHeD55yi2dqyOkpJLLfRhoAzilt5xPpFKKoGuTw6ojDw36+LPpR76SzyzXyYXbBw9QHPEx9VQ+jhdZ5mPrg8b8Q8j/MS6FqHqZMZ+8MYf3d4ss0BDxMQ1UPM1izzsM0BI/fUPQwb6qp5mHKdPZJkoTsYb23ImhEs9SF/Diw3dz+pvTRolU9WqR2nUeLBs9mQPE/2uO11Txamc6+hMz/rcaAh2is6iE+t95DNAaPu8j8D7E1XM1DlOlsKyNJht7PAu7OZvYBQNxEAPF7wwgQ9wdVc+yODtxbstDLUqmnz504r0KvRFep6YJlq3OGupot5FUujFB3+Rp4RCUzspXU/TgaqAMsWDByIWVolqHe1EzbKxe5A4HGblZWoGHIaQCvj0ITa2/g9EmN57GyhIlwn4sDgdXPo/zZMpKFvGmvetoQrp4385adQC0lsVQjsVHrGc8zzQ2UWMRwC5Qh1xDH/3yx0cnJ8amp4anxqZGJ8fG9sfHY+OTx4fmRsWFNmzP0+bmJcS0Zm9QmR6cMfUSLxSZG50b6hM0U2kP0Wfpy4gb38JiO9QnDKqRx+7z2UX2uPRTyi9hq2sxafeWtq/osc2F6dH58fHx+agrmMTKf1Cc1bTg5NjY/fnB+PBYz5ifiDxSvXPdNnsBla+iDPrM5+g208fF+USEv6ivz8aXhnLsAylaVNnOeqlWw8bjXbt686fuUXOCANjKJtLXgWz2l1kFntVXYXa4GmWg+WC5j49RNShPLKJ5mghcfIvKVyye0VS2zQFJEzwgXs/n86gMq6kdwNcvvqdp8b87Ddzd09VB/ibI6v6pmUQuq8rXIt6G3gkEdOJCmv3ujLE8VAgpu7ZNPoQFQPc86pk1ozUO8EN3JG7kUvHaSaPQ3SebJFWZwlSYZ5zw1QiJTen+roigmfke5fQ+KnkTJmPgdL6WlUdhxCWnpbxAtXY4RqyHJx1algzQ08n9EaVF2Kq0KN72JwF/U3rQRs+Zev1J1ojD6+rXqqqiDV1GlkZ5TyF3wBTn23keUu8wXfLE6/ZIWZQ5voDWy1TfjLJBep1loTUhBCNp95TizW4RadubaOLESZMoDnIPdjvwBkvssxE2PlrgxD2BpILvWhO/YL7LZlc1ocTNzrU2YKC1t4pqNb7JZjvH5ox4ilUyrwPiC1ej2Y/yOe4vxA+yGERADZFABixfZbhQpNu4vgZml9TeG781+ufE5jKLNDjlujuF5cJqg+9zrA2i+g3vuCE7RhEw9ZVocKhMg5faLMA2CYlSeBxjMLRNt8hAFoEtNub8oZ+eBx+csvgVPyM0teWWLqmo5AHE6N10ELEAwjpwSOUiLs7IK4wL8/CkCJJwxqy0nhm0iK0IUxm6GFAWpHSHPdsb5OGx+L9r9/R4aK9h8x4WErIg7t/DdrNWylY/jbs3/rtizeIv26y2yFiQavob12MhjAbfJfTOWomL/oKcBcezc2g355mbckjZZt6Gw5/vZhQyJm4BXRer86yS6qiPPjxDyA2jm14rjABjgw0SIVVDwRhvfse3kphHlsxHVhEcAQIJJrZll3kJCA0epnL9MZhotchzuRBE8Tp0zTieN01ppnB5mdxEDozD/He6zsUQ2gXYPvoenha8IXslXQmUdTlm7U9bplHXKMuqf97qZQ6R9CJEOM/SsQIj0D46a2iYnfOC5yN1/G9TYhk4eSzuoXhfpdruFipgAVQ8BKoJKr1O0zELgcczIk+SO4DVCSrJtU9dU7lHsklGTgqyNOWTtJJC1nMkIoiTjb5ZDHDc4eUgWMCX9jUJ/73P6Iym/40bm0NE/V0xHH0e5o9eL0OHWXBnmRPqwU4oOIur0YamrM28YvoYTaeKrJBgWFUc5W1Vccyvzm7i7LvHqXMFadY1DvZiP5KznsmrSqdy/04Hn75ZAnYPZXMrk9tmFXPw9WMptxTUA5xnhqG3nzVwc13D8aUze7tCi/4IJeeocvKD4VSwi+e1p2c+c+ODxfyNLkoaHfF9Ae32PV94TTLrmFeEbooEdgz1SyPFxC8sadVsQ/Ev8AlZ6g7yfzgmv8znT0rjOzggQ/D6PF5AnywZWhxgAVXAdSjfkMF9LtuS9gAUAZwDZ5+aRXH1c2UQ4og2whuMXWSuxBEYeOMUNw4EGW+lE6DxzrVGgipOnrrcDfdSJKIRKFYR7UAqA6BSgBSTMajyQDQBR2BXh4yDnAukWvvRHYTGsADXAORlxe2DgsMp99j+EyYedN08f8EeYtL7Cp4gnmOAGkqWv7Qb8HMDXhjQZUqkR0kTif0XZxF8F8yLMD7Jq6F/AmJz+DVekf7nVX52kc4P1jpGq9I7CPJBeaQt7helLglqB3wihQICSkYOb+Xw2rZ7gRi2Bpr8xX82T+WwhR7KdACWit0dYCfQUAfq6x4z0nAZUXKnKjvZkEF14NmCzuno7bEYquwSpaYKDWMRvws9BXEa7ae+sp7OjZdXiXVahmiq1dSMhV1v3UVx5sODkcsIFxommLtpj3FFWcSxWBaGC/A+nzhT0oOB6k5U/VNDbIoqmYD1EsTWxpWaSizZyL8/r74Q1/QkFh2+i4V9QKg0vzV+B2ls9LK1dW7hvQ6tDNAXMJYy0EZqltQsrtn2OA8fDjm0edt/Jh2119w0fpIsPsskdpE4OUicHqWErX6OHkw9cLx+43n3gVWU282n6FN30wIOhCg+8epw+YA9134B+43YbCvj1zQQWyNRt5lov+dPykSKC16SxvqLMzl6/EqoFwg6f9AARY71BTwq1rghN6Raa1kxIOG+gpnQr15Ru82pKtyPZCUyo3eQDwfoOrtraybhrMTq8R8nhPcod3htRoUIycCA6gbpc6uUEMCcj9/CJ/+vQrPsSeESiW8B9byN9BbwKeNBmpDLXmmj8EPke88fa530s1wrwFdDnlrVUHmJBvO1ZI7OgkUmAqauXgLbMvGKGeyShQvWyNRA4NHDgBPeCSLO9lQdewHZDR0ygdRGW+L0XiTCsTr6qLuRh/OLRufS8CFnwqW6EKV9XvD8O9+EdpsllZ940Uro1jWTQA6belzLTpj09Jf/4n5D09RsVbnAUWFHSsAGdPzff0opsAt1pXEIfI7XEveYOjEcrBJJAkWhz1SyA6NMhupOI2hHnIWWJQlTrj2sI/QBkXv21GocUIWY3BCA15GjaydUNJWFhAVIRntawXpIA1EqQH+ZN64RuvN7R8NVgLAdXw9cgNXwfQFRFbaKiDUAgYRkOgCszUKNzPz9hCP45hxcPrv9PpBlug3m1czV3ybzqq5rXhOKdV33JOM+F/PMyFO+8RH2ovEDwNzNP0+oQr6shYFoNVU3rs75pNZRM61uKf1r/5JtWaf3PKXJe+LoiAfOKVDUvI+SdV6RknPmiecHra61Uf0IR1goiAkUEET3KMkKkTi6ZZWNVs2ys8c6ysWTUTzH/LB+sAVqgQv13IwWA+K9kPk1VzeeHffNpKul/uGg+/6XG+9ZK66Mcvp4Js3xCsZsJxa4HlTF03VARPltDVHaLvS4MImGQRzAjACwA8h9y3CIdsRCS+Cryqxyhlhf99BZ1OIqYRHZHImdUNHMF4VvwU7wVE1QVxr8PE82Hr11xkaeX+NuQcSH5hquSI/6nyHDYFZKgfCT+DmxGLvP4VFp+gUcttIw86d04hy3F5lz9Fs97y2JObtTJjXE1p7wcd3ITpWGLSBCimZlnkMdCaoopdcBjodJNqsfUUBv8917tDJW/p3pUZvy6znN1X6hGMXfI9xktRuyT6YsGsKCaae0Kon8ED+rqJbAnrg39GPMxoaR+KNKQBn0OIiJR/sQtupHb5N6kFNhBCLqs+AeY5GRRp+ARiJQLGoW6Bv5N01qu34lVkDO0ZU/4AhJZUi1TRJDSrJskb8sbdNMkgRzX2sJE4kgixcmg/acwuc6CWGZ8Fefwcz5Fn9O1VOTMsrQl31wjS5rEB28XusnG0NaiGqiJ3QZ1+P2WGm7bWK9sgisZ5qodGKtIKHKkiQIqCJUI7ghHw/nhu+1BdzhUVsMJwL8LwPbqPyg+w8eIUGUi1cXjI/DYWkRyLUVlHCrenqRCwoSpGQUYtlS8kAqhhbi/Zsfz1NtfLVt5kwIk1Mw1SwEstXqU1CstIqQA18Rw1SnabpF9Vo9g4bDMqzlFrzmF4hT0YC3kxgUnTroKHqzqaQrRgBi1nrDfF3A6PCIWDtZAUajaSR3TK/ppE+qYBqnuIGc599G91lthelTOtGauo/0Vcvc7OOY8gcw88r58LG5oFzxWpMxYZDtWdkBYINeZggw9D36MyyRPbD263omVsZsz0Uy5Av9nZzO7nRX1IlXdw4iphvrb/DpkZFJeWR0yoz9fOiKc9Z8N5J+vsGAmVlSRHnNeVypZdionAWQ5w7GHAzufBQSOelnZ2lix+/EaJ72/lLPyOleV53vLTWFn4BSIjxOdqfT2irXiGzV6I2URR9mICapg39BiRz7j6/QXX/XkIlKqifMpnAJMz7ySmCALstJlUa5FcPC1SbFIgum8djnxpFfPtzHLsWJrLY9KjQI2cTVjkc2XX8yBq/AQC4hmFfMGPlnW0gXVJjFH2kibKXPZVG+KDdm/3U/NVGsS9tN+4oTon3f4yZSoQ6uU9W1DBR0peVylmrAqgXnf5EQu0VJkEII7RgRzgq3MdYJaRudx7nI3Ocn6o7KSruU0bpgC38gqpV1W4OcPkHZJEe0SJO5vJmqkiUhKtK3qFTRIDdAsXfCLHnJSIRemGhGyxnJLeGkLxc3opT6D3HzexapUHOiBbj7n/NExROlBf3QMETNjtz86hiht8g1DuAm/yjkKyCbXluv2+RguKDNDESKATi5otuosKPWIrPXk6pB9rUQiSeDS49OJS5YLzC6ghkaCx35ovD/+Tkm6PkEpD6V3idSNfBn+EhP6XDk8t8ShyghJbi6uln55bNRZI/ZW+ZgN4QCPxfex15zHotc7sfmVJijKKw13skCl4QmvunBbQJ2YrIMKwLvtsIfQhxyw1vfYW4Wf/bgo1LLgIKKU99T7vmq38OOBW/jhwAA3BwID3HTJ2Gt6Q7ErXYS9gq50lUXo+On8IvQZ0zbShWUtw4Mc0/78DL6WJvkVhIqFOF4qKNqx+DYXSgMeUy/T+G02l92wwv0N8bLDBP7MqxtGZYFb1kVElGMZRoUi3nnCqHi0tEst0rQuhMI/1L2GfDFPVn5REXFSZq79BwVN3UI4p8lbZL6HRm/c1hWFi62sF+MG15HYHGXTfOB2Hnquw/W38+oy+QSibPUwBgQmSa3j5tNF95pQCYhWccTM8kjKt5rJCaiZ+D8bNZkYyLmbCbM2vO5mCW5Pt5l4Q4RZigJ9QBEwbw/hnV7XWPFWixy0lwZtxbiGa600botn3Db4dDsZj7ZCgtytrMfeIlWnN/+IEasFLGMbTe2NIWSFt2JV4CCJL3RB607hyQUcIfdPAxaP+twNfW6TfTr1r9uhwEGJZfwjWE7baTm9EzlAuL4C/2ddThDnsYNz2juFklWxVXcj920ckLvRDDYEyHnI8HsUB4VM484Co4FxyB2a36NkJfHqxp2JeEQQRPgPDx6wHPBCYZITnt7463DuDSWzmXlzgRcfGbTyyen5XNJe6RsE8jw1bep9gyktswCZgdMzfYN6NmNMy65M3e0nTn4VH8E5oK/67jTMTFswrMFH4vHz8cTpc48fPXN6BpipR+Lnjp59ZPdhmKSf13zeeePEdftZkREfv+raJHpjBl4jq5X1RxYWjgdZNQw2KZZL2SLf1H3BYQKNE8tVD3hSrI5fT3UecR3Z7TgrZfXhrpnOSfW/p2vvwqtS6rtroyTHOsE8SP77C0w4xMDSAbrE4K5BhpZPLnJzRFTQxzHiShwFIXHk8OIY6zqO9gBxNA6kJjfgWbIiRm6tuObC5dMOAkayhoJWcD6KuCPcJ0tpHrpXomQcd9lMa8vUE0YF51uTduU1JoPqmplly42HS+HEw3K3xd8oy5eBxeSjZPlvLsja8Tfg5wJi9Rxh9WCKqw7+cjFyK1y1C8cc7qpTQ+zYJqWJYue2KVGqhb1g+JF6oAvaBVMGdULbUHgsXGOEyBg/nUPa23ebWrheddC11Z0kIlakSJf7qkgRsddT5fPuuQgRj2O9pE6QBKlFUgJlvk1OLMMQmcu3CnN5FwW2oS07N2RvYSLS7SnvTJw5rOxETe7MtR4FaYx6MoankxGERDvMyRLyBVhqE0pSad2/SZhXofxXRs8VBzFESJAcIWw9TCbxIWGOhQ44eN3DEpsp04uEgzztoQaLgFh4CO9s8RASUSYG3UKDNhIh0UjjRj3j4kF8nfQut1JgX8Dvw1xOuw3pHdIah1DeTbfRhJ+Ih+2y8smQtyH8m3WD9GIzLvgt+UaE69WN4/o7Zdr2BYBLYWhTIoN9uZ48nLDYoEg1kD7wQfkjLpS3NbvgCVvrmAcZuoM+ejwYUlVP5g0jE4w9PbLc7ygyosF9NWq1JIDTBg+Y6A1GsCfMjGkt+hx8PfgV0EOpuNT73V6WWHHVwaOfx+S3mZQtOtgz/luYfBaTz2FSEVe6vgAkH+FRdOkwOBRBxH8Zy35fIsf472Dye5h8CpM/wAQRW/wPMfkjTP6YBQkQfhN+3lVTUZ4YEW5dbY72k6O3VkJRCsXM6iAUVw6tRQRaawq1+VGZT0qFGtvXmJQqKK6W3l4kvnrFfSrLQ0JksALEVycNDB3pl2INBlSN8aqiSkmTIDv5UX/vJ+OXLwRGthrzd01UMtkHBkTJKqnon8b+gFYTvNUFDGLorx0U+WvSO8Y+K6jZvQi6haGT1hfhoRHCZ2ucuEnVBd0KEub9DatSmPefA4V5LwUK894bKMx7W2C06pQn3tZzRVG4eLytnyiKwsXjbX26KApXI5X+gTcKVxMXHTYXiw7J3+QuRuEi0f3kBuxyMwGxuL4oF4SpJyTn0kKX6FRSVJTgBskJtIwmAYGN3ZOe01cb0WEG43YmFnPUdDHnve+RT5IyqQCLsGTp4cT+ApfeA7SYyoeBDpRa1jGP1LLjbvMhP6lcWa1RKrMiQOijDaN7wAd3/VVQTihsWFqkbQs5h3EfE25/YrfK+Omu4PJJElU2o+DyPHEjJN4TMZlJZFkrggVhATqXUHuvE4ne4Ynh7MrhvshmgR63O7FLaNMN97oEKY59cq8KnO0mKY98mgL8/Ljz8n5AkU6zJdVgf9Yi49Ejj7v7OScKdGndx6HuZqr114o4FK9XsDcK8CpBTfYwjI7m2pY0uy4jRbYiW+4dbrxT4d5RFsRdILGouiwGt/1A0ivY9oNT/BtjG1wBohBvIXfS7BFiSQpZLfKM2M4cSpiEV7KeywUhnRBtLn6qySKvgIn0XotOvAoipOHJZ0zLL5Jy+q9KDFWsLyXzAPXmInzjZN7QbIwaQ8Rsh7/eRTubyxl6sQ3B0YxK0W7UbDJZyOehwjpOuxsn5ssKwJx4Mjw+vy6BLJH2BOjJnoAEWE9JmP2YsTqX1fL66YwNEy/k+EFSj5w/wQ+2QuKIBGJ5I529YXhO1CD/0TpJMXjMIekgGViYeAAbnZz1FP1oAaD9z+CnASC/dbWYqgjx0zI4XdEpbAGiJKZqJ1oe/oZaeUwWJxoLP0MjSlS+t4QQQcSLCBJ3GxF8ExDB0+sgAlcmdVhqkERwhkZfxEauQQpJDRIZryNOaPb4/7XSDP8nzbBFiKyEAWOby1f4BvEcBlArB6mVg4RJrdYu7O8RCdVRBMgQeQK2S5c7FwklCIF0AX7ZJBBRA7M7SBjUQCH/CRHVU9AYXiCC2SH4xhL+NACfxW0fInqjMqtvIS+9DomItuKUEBHVowZMioC2eZ95NlNwPl5TSB4FUFItcx5q9TDALwIRHaS6OwLrIlaJIvIBxIJ1r1JdlEXZW/1YRb23WKUUO8ho/Q4bUwIh7yC0nDdEenntBnIxDsD344Ui2ReGhZ0zRDQ9qxqHOeS8pCOcaDZIjnD948PDw/uL3PyOByNOjjI2ijo3qMqL/y7zauCqRqDfLbhzHdS4bcOocawifhyRiI8jyWYmmZtKiPIvMPkaJkWoLyJRn7D8t0mARagum/OgwwYPOoz/Nyz+axbEYf85/DxY67hvFHPYEhcGW/lL7LipKuwYjBN/8G7jxPtDV1bf8prDiTIKGTcNQRMQx5K/XQY9dmfIp+Sx3WeO3T6fUp2cUj1DxqyeVcSH4TvEh1cC8SHFMcY+XXzY6seHLmPWQHhrW+BreVsRPhzz4U5/3cedF70Qchkzfsh2mbcuUKjDmH2/i26LGLOd9w6FBsc1BUAa6Pz98lzPp6vCocL1PHsXfc+DkOPkPUKO6xIf+IrLOb6XCSRwxxg2oMYGMGxQ5AKBYS2fOsdBr3cXcd6hgqhaxBkmfAdfZh2E+ZeVsKYnNOnPMyH/A2JkgXwluSLqZzH5ZCCy/BLu7dqyCqHyyFIiSl56h6xkgxdtPnm30ebfAyt5plq06eLMCrhSmB1Ukil+RGLTmWvvdQ8Txvg0YR4I3Ms+BiG/1bNSDllPQkaPHJIXoAkEjUnH9CLniBhuk7ztRXez17/IZOAXC8V/cH2FhJPdaOToCid7hK8ZDrTJwYGbpY1DMQ78guJIBIurleBAJSQPniut+7gzuzEPDuSfis4XLm1SjAMfd9FxEQ7cfu9w4CsiZLzjcDB3KpxcD5FwzFDOsPGOhZquC5+PMeuviDbcRneIOKpA6t9xAs3KyIdQDoJ9H74Z8SOdp9bHPO4pvzg50vy6kbG5fQLiGh5ftiUQ6+CCeQmxjr4O1uE2dVxcuZOs6RxMQ5ZyG8I2jV5s85G7jW2OApP2mdc0k+YbsN0dMCwHDMsB6yRHV0lw+RESbXYJTNfg6b+BeDffQwXa85+VjF20WNAZLWHsol7GLlrC2M0CZyffyd8QpruiXKnI7dVX4PZc6ecbKnB7xdLPWxW4vWLp5wdd1m3rq8a6fVdJP18ZHI2WBq8wGuYE/YZw6quPTr/jBZhG+o4FmI0SIca/jgmZ3/0PTP43Y2yjqPHL8PPVO2PItt4xsgxmyLS7jSK/BQxZvFoUKVixWyGBWNyI70GeaS5bFi7HltW6bFmdhy2rK2XLPCE7nTFctqzWZcvCxJbVlrBltV62rDaALbvtMD6rhKxuA1t2uwJbFq6KLfuTDbBl9VWxZYfulC174+ts2T1ny5Y3gkJK2DKyotwoHnEbvWbZsu2sMlumvmp82WLuFeLLUASYyaYtHuDd1aCFqJyMHDOEg0rRz2342QUPZ82vg36iFOv9dd7sdd7sdd7sXuCuSryZx8L/dd7sHvBmG0KsVeDU/RVxaqaAmruXg1SLYjid1ZYNQpHi1L7XLlPGjdxfWabsGw5OJKbs/7IqmLKvwM8T4VeLKXvdbWpjoBLdGwLcpo5Bd3FDo8VryTNlL2QtmxTuAc5T/gbcKoDqHwioP8rrH8+m00bG9nUf5OE05q/u6TzILWt8EDatZakzRsqwjfK9TgyqRwHO5SRKgOlfLxhQOTDK0eSgejkzf488pPCjz2Xt9R2k0CX3ufDrDlKvSQep+J9i8vL8o/6RCf8oWPmFRB43mPCfK+TEpVwsy1ncHc5N91KnjZCDfcBPOqRFzw+3Eis6jtaarkcU9BYQXg+n8lL4Tj2ifHD5pe8MuOwFye33DiTvCAbJosYZc9kIrBJzq2RvGERJBcBdUWU2ezOwkzGnxiltUQvsZNypclHTA6PGTTg1jmYW8qv3JCgc7YX1Aeb/g5/fxkXcvwGAWQou/6lacPm7HnB5HJesFnLA4894wGMCIaLn3vs84PBNCAE9997sAX8vIMTz3Jtj7klQP4WcpefeCbrXQvc+j3yc5x4Hnm1076vewHTtHHh2FAPPzlcGeBK8OXP6sUcIivKr848/QuCUTJxnz88SWKVbp46eOkrwlW5dPDrDHVFxsRw9dzL+xB0BWze2XY0ixrHNHD+hkFYVYVkXOmrLllm6sLDtX+LColNgQy50rKsidaCk7xTYj97tQ52PK9XGr3HjnofY6leZG/JOocNTetZCHMFWDIHXiovPL2rJkjCmlfViSLuZawlxqCzK/FFWw3UGYtJRivrSSA44dAxrJz96VYyJh6mi3GYTUzHQeTdFmcFpbeZVT566/nU8+bBXHrtF4qOn+bFbERFORrF7hKRkn+P6+WGFR5EJqObINrbdO+zwAAuUbcyo5YJn9/tHFw3OoO9KaeX1JCC47R03GMPQhQ8MnUxS7ASzMZEBP9YZuvQY1uKbGcpLruKIvZozAk2bW5kjNXhS9Gjia+NyB5LhqgQW8GgmUdEFC+h14hEoyHfBA6aoQpZQjSSmx/+m4Zu4UKZ3o1itGkE4d5FEgMT5/UcxicLj8ugqbjRnhGAkM6ATTr0OJIYIA5YWh7VmF8lThPP77wzEoY0wQAsMzQ81LRsXBRn8PRT9JEJnPTQru5S9dH5n0Un2r5OGr5OGd4s0bJJIfGF92vCb8BOre502fK3QhvFaRXLXYUWy2HWK5LPrFclsNyiS444od8hxu0RgpyJgqISusHZcCjDepAQtHWz0aN3Lpf4avIDwS3eb+rt1R9RfKelXgeTTyblbBPhw6cZW1xU8tJ7Groboxo5SupEfO8fVdAnU7HHiD0MkOy4AHrqxm0dJ7hF0Y5OHbtxM1v+9nG7cgoe1Et24zaEb9ylAN24vQzfuKEc3coOSnSyg2qvhrR18FqZz0OnLIxtfC45pauU53BgdHL6b9Gu8GQGHS7uuR0kH0raVCdl4iyIg2z8zOjbKJB1LoZ2qpWUdI454G9Zrx4SIV/TtincolcnYLrifQ5g9UwHdIyRHrVRztcSsD4b/6t2G4XMVYTgRs2WPLIsIQz+M7kqBYAFaI4NO4WlXvywiRHmBdY0fWNei3nGJDg9fIqMAHgWqBFgvE0vvAOsni4B1u3DPeppHUV3qpDERWHcLBNHjB9YhDqyjFPN2CwfWWwlQtyGg3kZmgJuwYx+g3u63/NtHRg74wj+leANv+Kq9GsYL4ywI8F62HE3+vocO75PFMEJezRg36ajBDYsGghsIPZsVEPl7Q0gB99lDMj75qydYKAbMqFwdSopnPCKCq25IrMDhcFMRHL438HfzncHfd6wPhClgOCqNPPB3fahLQoPlNAe+eKYkB7noRUtyl/lSwIsM0gvrAd4wgd4mMgIoBry7ggBv1At4v323Ae+Ldw3wblVKAW8FgKvzmHsdRGKLlp5AETX8kEePzyzvoU72QNSyONnDB7LrUYDaC/CWg2wK7g1wtxct3jjIjnhB9hZGp0NvFSC7zQOytxHI3u6A7B0cZO8kkP0ogmy1DMjeVQ5k/yOB7N0soJoDsvfcO5A9zYLA4slCRluWYW78YPtyxi4sq8e0vGlhWigPujl1Xgpcg8l5B3S/gpD7ZdH2D7EN0Pb/XEj7MhjmuwudRCQ6KSLpg1CKeywgEfI9AdS8H7XENweKYb4FP7+MmOXRKjELJ+2rwi/4Lhyj678rwS+ngvELoJalMAr5PJFX6RB6jLzaIDACgscwQNYagY4iBON+kNBRnYuOXHlGI8JpumgqI9QmkTUhoC4SZQMi6ObhSoVzj7wnJtjMPEiGT7BWTjDMVr4uA7XOXPuyJN/5cVQA6dFEmvcSeBQV7y0ie4uy1VEmjqJChuBWIxPxF7oBQ7S6Bw334Im/gFfQMPz6N+C1tNFr+XdCHVe2BR3ahMiqgU3C1KhpLQqEAGdhB7+vONbMnY5chgeVhbpX4P8sl9oU361CYnN/ZciQNopMa4Mi6rw8VLQ/EC9QfG8JWyWU2GuVMZS+aGt5cg3h4TdVi85lkAAIo+gMr/ecQwiBj5QJmMMPklgPiqJO9Qg/NHeamzD5gTgRrOSOQsE/5SkJrawI4wSIUGo4rPUKoMXDj6dPcDPfAGDtAlJH6jKRjtMr0tc7+rUaOF3x4Ib+TeUgdVkwXPlEo3dIIH1pNWfwsKuuVfCYhM/9TRI0k74wo6XpN5VN8TOE8EKzCtwwwipYHE7jR+Zn1pv5LDnWcN3icnxLINz+Nvz8pR9ub6JwBi0l0DtCkJqfQh9V6sSxQS3KXoLczcIguDXkwG2fScVn7zZfUFm7GBwzpzo3GbtVespAER5f8xVWxj2GYuxy7xgPSf8Lbmydl6TXTAeBbHKH6UV47AsuF+Q9A5Aa50HPjHN4K0bZlh30cM+Vzf4ee/2H7Cnrt9hS3GLWsb7wPei9trzYEAldreNjXhgdHyFqNZCGxk3y5DXu3ljkkHcuKz1FVNlRFYBmg0f49FX5KNYQt+EAXFPWzRL3v+9F3u9nAsowAMEtyhxP1+JWVgU0b3Mht3rMyC9qlplaB952loO3dyjofkKCVA5+EdK5xhic2iUQT9FbPylh64JmEdVbCjNR6dwBHVjHHJgZJL5G+NgtnCS4YwVSux3kWNEUIvcKF1bWeWGlfrdh5V9XBys9J3qiXcap1TWPEtKlqjmsUiSsCrGVC0RYNyHEmyFhC4d/APswB8SsiDDWSrKWcJHUggAjp2XDJKn4dTbLn5TToXuQjCSRRDtdnyayshOfvEMcrarYna5IYlPQHQJh3fcOhG1w5/e6rdHPSW6145fiZ+4/fse+3UQHXpZ0As2pum4KZYQMO9xpyrPAOFkmCq+pFgImdfqwWs5962WTZ10bBhcVz5Uk4wNO9ZJ27HRGN1Y4lfYXDqwhAs0Nho+nWMVzEnwQfUZvuBR2KLBAphB2PFwBdkSJV1bgnqS2olALz7yvcVy2gm24PsZe6zZcXvOttnu3/cocsT6bN21D5affkawrwH6L/BBns3kdT9imc+ECLLiOJpMwK1s9vmgkl418oI3W2KB6BrrggsXA0cYH1Qv5LPk8nixoef2eHAhF1lmJlGZmKploLcFPAhduX4WFu56B1n9iVRpovTfQ1+ltgb5OqUBfp8cDfZ0eDvR1OhDo69QlY7kgi+A3s8JXebf8l+7EhqrBAUz7pPkUlxzEf01+5SQuzIS2DIsUa6No0NJWNX5ILq41jycSlmXtRSNfugyw/xu4DO6jj7ueK5Iwr6r1wqiW1w4nuKZIi72PM4JYjoYIhX3U2fdIbXwzZxdbfOwiV+mEpEqnhlQ6rUW0UxtRPTyYTskA99rrdIgF0fMcDlr+U0CrXcvVoHB01q9CbCWEThfOX7zUV0k/vEFqKljHIw49PT0jWRY3wDUh7/aNglO+BRFSVpbQ99dKOEucRtpaoN+8YZHvd+muw235Htx1gxWAr9iLsOu2Cql6s6QRcGX9ttx/Y+G7vP9+p/bK6kdq1yUTvBvS0dbKkFhoJ8jVsni7We6uiHBkQSmKFEqIs2vahKAEBeQUyH8XHqdMp9gAb7AL1ah1mNuJByM7M+kSm36TkJDbEaGSvdVIeTov+VYTwlAROmqtyem/Gc8zlv230AX230oQoRF1tvAwwMtgSkyQyNTKwlpZ6FRwboXpkg59Xgt7/hXdUvCpMCW9xloDpRGqUEdpPaUNlEaoSR2lpGbA8loqD1N5mMrDVB6m8sDOlTKd15TpvLZM596Hqpf9N9Atflkv884lv9vgqRaR+YjM13v6qZGtamRJrSyplSVhWRKWJQqqSTAlY1v4rnhZR2kjpRQ7BzM1VFJDJbVUUksltVRSR2mj7KpG3mqksRrpX5Mcwumkie42yXGbKW2htJWaNFPaQmmr6GT+c6xbcM+32tjKOFtrQ9OAZQArPbWYr2M9cIOvzDXi2tdoy5DlALa8/pWaWWzdTq3bZevLtZjH1u2ydZRat/tb76ql1h3UukO2/qFazGPrDtmapJtrHf7WCd66k1p3yta/U4t5bN0pWzdS605/6/fXzuLtZh58h8MkfowTHitOUXo8lsAtwqhhvwPdhsIKQI4Sk+GWV81keMTT2RFX6maZqq7ZmpoyMgvLWk61uXWZbs5pN7VFIs3LSPdmjJxrD3GIc+XuoeDBZ5lTw0swlLboaRms5qK6x4wUml0seGoHH7NBtS9AzQUz5ZvW4cDql7CmllLPaItmXj0s9D/GyiF1bWbm7NknnlhzuyANl4l406QjBvYHvMnR9GNaKqs+mk3Pwc/Fx05fULUlTT10o9IbvKAltbxnqkHHLJU8WXGjmSqej7ep/JQbJYC+CSttr7XXimLiZL47Ev/Py2ha/c9rLjGRv+R62AVGf/7+CK3gALHaxcDoTOpeC+FFNbT+OnGc+lvvjK4mqR2JOEigf1rS2lwASHI4slJ5DyZ0qsiPM2EKqcdpTDRdoesFShe5sB+zS5QuU5qiNB3/eyaUpzcXeDz6DClZbmbzOlcQGJlSSh357ZeQUl8JpNRlCCYZNr5J/G0mWt21kImKkm+zbwNZXEehmXaGyv1i7QhZzbS6VjP4Ch2e++G7HarwX1UhF5RXsAKB1Mc0RGkNW93r8XRyzuXiMyM2GWh8boTIZ/ZXNLMihr3RF6KwWbADQC2U+L7fRiJk5tofow0mBu0jugEYeUfBCv/eGELrmlvEZABVyDUUEW6Gj3wCd3SKSlaBBx1spDOSiWHAE5abSFP7wwrqRjZJq029k/fXxfsj23k0w2miAITY4LcUJGbcBj2lDdDVy62wubTCLHrbt6LXFA+AS+TSFtYjykJO2VanrMZvAep7q/da4es1XvTTPxhAroRfL1hGHo+KWstploUbtAxF40bl82oti+IAUqUNHatVRrwAJFdes7P50hE3iL2fYa7wZG5Ay5nFwhMUmgxpBXtxkN6tX+sTG52cHJ+aGp4anxqZGB/fGxuPjU8eH54fGRvWtDlDn5+bGNeSsUltcnTK0Ee0WGxidG6kbz6bT2v29JKVzfRZ+nLihpG3zCx010fHvk+TbLovlU1qKWPayCQuX+yTb3/aQlEHtpo2s1YfAEoDXoSRsGBS0EUiCTM3DWt6pM8yF6ZH58fHx+enpmAeI/NJfVLThpNjY/PjB+fHYzFjfiKOr5fkjUWapjOmR8/kSEgRNKtrKi24mzdv+l5V/M2BXY2mSWzv9CW72lNccSQ9YwYMOR6MSCkuYslaxVlPiyewcOfIGzSHaTEhsqmVd2DQadFPf8+dIc+fltiSo9EPYPLDDi4tK60i41E0Ge1vlkiWkGAKHiL+Y0wIsHTTIKwrblk2mYXljLRpaYtUmDaWzfhHsAskDnjAX1JG/igLknftB8Dwt4hFLwViUReH1tHfGsCYvZ5ghlz2tUvppuC/iF27lDZMoeWm0LTXPsmxK+242xjyJ6tz+nXR1OoXSk/3CtS2P0Xa9kbUtmektr3J0bY3c217iBwAWkmoVoeoYakNsSBJtOoIl4VRhiY18HaHONQRDYI66DIsL+tRzIX2QZ9ms4B07E7s7mkeCxd17dgft9u0N0kHB1/Yd2+E2/eQ8r4HX2Fx5cwa1O2lWr+qiIDuWxxsvjmwyWkeFHcrW9pGDb/mxpbfzmu4VESzG0u+pB/J82+9dzhvg0ghxtaTqJN/wDomADJonam70gDufHDQMx3Bi5bzHyhFcBuyGmpw38P0OkFmPR7TFGQ2FjBOOQ7GfcxqcHoVwWYDzuCsHIu22pjw/Ts2DOQrmzQ0CLjsOgS4fJQbpNbVXrjhainabVAYdzeaDcLswiJniQo6N0N1LCDKuAscgNJd0I/1xgoAHsG41wSiFe61Q9pK5zeGRTza4GjtUa8DAU7NYYW6q1I/arUC0IcrAnqysJeAvqGM+jGynomEHZX8CvMEA/klBNcI8RsRsSIZH4LeL3tCgvw5aiJQRcJrhHiNUarRQTX+jkk/he1U2kmljeilQKX1TOQI2HXdO2CHNHeAPcYjGW0uZdBQAZYYM0BP4O0NWUVUVtM7kfDsfMHgkfBwpcxrKcsgVTwpPylgaeCGPFtxV+KTC2PCp/jOor2DJfFhRYylLdvmPLfxzgZIFO6Hepdwq0xgaaiy4QXKDuqUtpBMuRY+iZ8BH9IxxMDZwfKEJdGNK4yWK2cUcTnRJkAetFY6S9bg/ui9SDM/R6G9N+Brsdfi+tRwJRjl6kQ5dTioiFdXMPWSl8JjrRp2Ahk/U1/B19NAkISf95DEaj7y7h8Y7Xp4YP6MOj2vrQhWGIiRbnhOU8KBCe431A37fAKjqdQxTkMtkeJNJ72X3sBJpBBXOi7VcscfnkU+/qNMEIJRSQjSpoct3yXMogBkCHJGBs09T/IGp4u/qthFW2AXpJ8koOK3L7D+JdpuaHmT9tD0m3YP7z70pt2mlbAW0XXP0HcfUvdaD+yWXJoJBbun5iYPjkyNJAcOjs3rA2Pa3MTAHLCNAyNTc6NT88Nj2sRccvcDu7Uk8Lm8xV4LrpMp08jYiXTB1mynr7nh0ZEJXZ8YGJ2HZGzOAF7W0McG5uZiU8lxPTkxNje8+9atPmEEgGFz+/RsEhpPj4xNTg6PjcamYqMTkyMHR/uuF4z8agJ5/unT1kXxABcN+6wYsc+y82YuoRvzWiFlW9O4vUVZppBKiQIf9yrmTHZc0HcyqxvTUDw/lwCOO5E3rie4NWSq4riiOvSbMvKJZApY4uCa5GWo5XIpM0nXQysDwK4OINs9UMinjAxOQCfnxOPZjA1TG0B/EVrn548Crw8fi6LPYz6bN5/ive6uvDep6HqKyEDi0hYNTQfOnugd/2IgiNhVDoB7vWDLk4dHge65Aax/VWKUzpIpEBj2nSRQbijgzCmgCx+sjZXSWTzU/inFx/M+KsGPB7gXWXIUUTsIUQzCUpy+IXr6UcULtkph+AyUvgWBlAzg3K1sJg+aBiJqOARHyw3/VVghyi2RSGtmJpHoD8nvcBnA3sDRBXRyncXlkDPy2tDU4MFhtf9oRs9nTf1BlQrVs2bGHBqdGIwNxmLjY0MjI1ODI6OxB9XLD6qmvl+9kDcsOzsUGxyJDY7FRtXHuZBnCC5HJvoXnRdTJzEcTUiHl2ybsE0pTpeW0bPp+MNYg47xftYB7igXiT/tvGy0AbJxQaVhS5q5fBZxBNC8g7lsNoXHGvB4wqfTuWze5ha3+EFsXBfSx2LQWMEY2rjSOTEakh8lb6Symm7jOrYMW2x82kUwRByRp93O7yUWYcopI5HPYrhtwsEncKHJts59Yx5ezyJVSOCeosmfunTpQpzfucAfAWaLH0XTdbGZaM1wkpwWEzk0fBCT92LyIUw+jMmPYPJVTP47Jn/LJNX8vzD5P5j8HSaIveKt5KiACZKw8V5MjmDyebyL5j2c8kC1TvxJTFDVE6ePaGFiY1LA5HlMbmByExO0Go6jwiL+S5isYvIZTH4Dk9/EhA68+CImf4bJn2PyJUxIHvVlTPBMJjqCgvtaYNByCvpMAXopdCXF+eNh3jAEEIWjIM9hckMjvwoykOYbD00NyfKJlCokEyK+gSgivpGnaG0pYlkmCC7DPnH2n49mwCoPpbN6IWUcRsLCwtX6otIGBBUKh9pD8rcNfpF/QMHRNqWpJhKOhJuVulAkUqdU9bcm8mBkKNIXORnZHFEj3x/ZEzkQaYl0Q+4hSLsinZEjkcOR3sjuyGhkEsrw/0H4jyWbod19lO6Dvwfg7z7I90S2wd9jkRFocV+kvmlrk/L/AUMyi48="))))