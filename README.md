# lambchop
Generate realistic user profiles and avatars using OpenAI's GPT-4 and DALL-E APIs. It can aid in rapidly creating OSINT or Red Team sock puppet accounts or simulating user data for testing purposes. <br>
Free access to the API is not included, you must have your own API key and setup as explained below. If I could be that generous, I would :(

The vast majority of my work on this has been "prompt engineering" ChatGPT to get the best outputs. As such, my testing has revealed when to use GPT-4 vs GPT-3.5-turbo. I highly recommend leaving as is for best results but if cost is an issue, you can change the model used in the code (generator.py module).

**Disclaimer:** This project is not affiliated with OpenAI in any way. Do NOT use this tool unethically and keep in mind that creating fake accounts may be a violation of a given app's terms of service. I'm not responsible for you doing no-no activities!

## Features

- Generate detailed user profiles including name, age, bio, and more.
- Produce social media avatar using DALL-E AI image generation.
- Support for multiple languages and countries of origin.


### Coming soon 
- Generate social media posts and comments, automatically posting to a given platform.
- Do that ^ autonomously on a schedule to keep accounts alive and active.
- Lots more cool stuff.

## Prerequisites

- Python >=3.10
- A valid OpenAI API key (https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)


## Installation

1. First, make sure to set your OpenAI API key as an environment variable. On Linux, ```export OPENAI_API_KEY={your key}```. On Windows, ```set OPENAI_API_KEY={your key}```.<br><br>
2. From the root repo directory, run ```pip install .```

## Usage

After installing you can just run it directly on the cli.<br><br> 
```lambchop```

The following optional arguments are available for further customization. You'll be prompted for these when you run the app:

 `country`: Specifies the country the user is from. By default, this is set to USA.<br>
`language`: Determines the language in which the profile is written. These can be mixed and matched for more realism. For example, you may want the profile to be written in English but the user is from Spain. 
 GPT takes this into account and will write as if the person is a non-native English speaker.<br>
`style`: Sets the overall style of writing used in the profile. The default style is "casual" but you can use any value you want.<br>

You can provide some, all, or none of these. If you don't provide any, the defaults will be used.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.