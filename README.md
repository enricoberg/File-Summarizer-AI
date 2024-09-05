
  

# Document Summarizer - AI powered

  

  

This tool was built to be able to summarize long textual documents.
It works with files in .docx format that have a classic Title, paragraph structure.

### How does it work?
- First extracts the text from the docx file
- Separates  the text in paragraphs, titles are recognized from the bold style applied.
- Creates chunks of text made of full paragraph, keeping the total characters count under control to allow them to be fed to LLMs as prompts.
- Creates prompts to summarize the chunks and get a summary of each with a call to the LLM API.
- Joins the summarized chunks into one file and formats it.  

The app is preconfigured to work with Google Gemini API but you can modify the code to use a different LLM. 
You can request a free  Google API key [here](https://makersuite.google.com/app/apikey?hl=it).


  

  

### Built With

  

  

![PYTHON LOGO](https://img.shields.io/badge/Python-1572B6?style=for-the-badge&logo=PYTHON&logoColor=FFF)

  

  

## Installation

  

1. First you need to have Python installed

  

	[Download it here](https://www.python.org/downloads/)

  

  

2. Install all the required packages:

  

```  

pip install -r requirements.txt  

```

  






## Configuration
1. Open the app.py file and set the name of the file you want to summarize:
	```
	extract_and_format_text("example.docx")
	```
2. You can specify the name of the output file from this line, or keep it as it is.
	  ```
	txt_to_docx("output.docx")
	```
3. Fill in your API credentials in the .env file (see .env.example) 

4. Run the app with 

	``` 

	python app.py  

	```
## Contributing

  

  

  

  

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

  

  

  

  

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

  

  

  

Don't forget to give the project a star! Thanks again!

  

  

  

  

1. Fork the Project

  

  

  

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

  

  

  

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

  

  

  

4. Push to the Branch (`git push origin feature/AmazingFeature`)

  

  

  

5. Open a Pull Request

  

  

  

  

  

  

<!-- CONTACT -->

  

  

  

## Contact

  

  

  

  

Enrico Bergamini - enricobergamini@outlook.it

  

  

  

[![LinkedIn][linkedin-shield]][linkedin-url]

  

  

  

<!-- MARKDOWN LINKS & IMAGES -->

  

  

  

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

  

  

  

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

  

  

  

[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors

  

  

  

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge

  

  

  

[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members

  

  

  

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge

  

  

  

[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers

  

  

  

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge

  

  

[HTML-url]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=whit

  

  

[issues-url]: https://github.com/othneildrew/Best-README-Template/issues

  

  

  

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

  

  

  

[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt

  

  

  

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

  

  

  

[linkedin-url]: https://linkedin.com/in/enrico-bergamini

  

  

  

[product-screenshot]: images/screenshot.png

  

  

  

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white

  

  

  

[Next-url]: https://nextjs.org/

  

  

  

[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB

  

  

  

[React-url]: https://reactjs.org/

  

  

  

[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D

  

  

  

[Vue-url]: https://vuejs.org/

  

  

  

[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white

  

  

  

[Angular-url]: https://angular.io/

  

  

  

[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00

  

  

  

[Svelte-url]: https://svelte.dev/

  

  

  

[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white

  

  

  

[Laravel-url]: https://laravel.com

  

  

  

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white

  

  

  

[Bootstrap-url]: https://getbootstrap.com

  

  

  

[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white

  

  

  

[JQuery-url]: https://jquery.com

  

  

[CSS-url]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=whit

  

  

[JAVASCRIPT-url]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
