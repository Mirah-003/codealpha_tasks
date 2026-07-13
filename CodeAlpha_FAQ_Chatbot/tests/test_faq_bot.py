"""Unit tests for the TF-IDF Cosine Similarity FAQ Chatbot engine."""
import os
import pytest
from app import load_faqs, get_best_answer, FAQ_PATH


def test_load_faqs():
    """Verify that faqs.json loads properly and contains expected keys."""
    data = load_faqs(FAQ_PATH)
    assert isinstance(data, dict)
    assert len(data) > 0
    assert "What is your return policy?" in data
    assert "How long does shipping take?" in data


def test_exact_match_queries():
    """Verify exact or near-exact phrasing returns the right answer with high confidence."""
    ans, score = get_best_answer("What is your return policy?")
    assert "30 days of purchase" in ans
    assert score > 0.6


def test_semantic_paraphrased_queries():
    """Verify TF-IDF vectorization matches user questions sharing key domain terms."""
    ans1, score1 = get_best_answer("Where is my order tracking link?")
    assert "tracking link" in ans1 or "account dashboard" in ans1
    assert score1 >= 0.2

    ans2, score2 = get_best_answer("How can I get student discount codes?")
    assert "student email address" in ans2
    assert score2 >= 0.2


def test_out_of_domain_queries():
    """Verify completely unrelated queries trigger the fallback response below similarity threshold."""
    ans, score = get_best_answer("Can you write me a poem about Mars?")
    assert "I'm sorry, I don't understand" in ans
    assert score < 0.2


def test_empty_and_stopword_queries():
    """Verify empty input or pure stopword queries do not crash the vectorizer."""
    ans, score = get_best_answer("the and or is")
    assert "I'm sorry" in ans
    assert score == 0.0

    ans_empty, score_empty = get_best_answer("")
    assert "I'm sorry" in ans_empty
    assert score_empty == 0.0
