import io
import regex as re
from pathlib import Pat

#uv run pytest tests/test_train_bpe.py
def train_bpe(input_path, vocab_size, special_tokens):
    """_summary_
    Returns:
        vocab: dict[int, bytes]
        merges: list[tuple[bytes, bytes]]
    """

    text = Path(input_path).read_text(encoding="utf-8")
    #init vocab
    vocab={}
    for i in range(256):
        vocab[i]=bytes([i])
    next_id=256
    for tok in special_tokens:
        vocab[next_id]=tok.encode("utf-8")
        next_id+=1
        
    
    #split by special_token
    if special_tokens:
        specail_patterns = "|".join(re.escape{tok} for tok in special_tokens)
        splited_parts = re.split(specail_patterns, text)
    else:
        splited_parts = [text]
        
    
    #pre-tokenization
    word_counts = Counter()
    PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    for part in splited_parts:
        for matched in re.finditer(PAT, part):
            pretoken = matched.group(0) #return matched str
            pretoken_bytes = pretoken.encode("utf-8")
            word = tuple(bytes([b]) for b in pretoken_bytes)
            word_count[word] += 1
            
   
    
    #merge
    
    
    return vocab, merges



