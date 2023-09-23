from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConstitutionalChain,LLMChain 
from langchain import PromptTemplate
import sys


def YouPassTheButter():
    # GPT4ALL model path
    LOCAL_PATH = './ggml-gpt4all-j-v1.3-groovy.bin'
    callbacks=[StreamingStdOutCallbackHandler()]

    # Verbose is required to pass to the callback manager
    llm = GPT4All(model=LOCAL_PATH, backend='gptj', callbacks=callbacks, verbose=True)

    qa_prompt = PromptTemplate(
        template="{question}",
        input_variables=["question"],
    )
    qa_chain = LLMChain(llm=llm, prompt=qa_prompt)

    constitutional_chain = ConstitutionalChain.from_llm(
        llm=llm,
        chain=qa_chain,
        constitutional_principles=[
            ConstitutionalPrinciple(
                critique_request="Add more context to the previous statement.",
                revision_request="Contextualize this as if you were a human.",
            )
        ],
    )

    with open("./brain.txt", "w") as gpt_in:
        sys.stdout = gpt_in
        constitutional_chain.run("Solve the problem of why life exists.")

YouPassTheButter()
