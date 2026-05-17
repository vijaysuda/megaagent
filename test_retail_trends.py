#!/usr/bin/env python3
"""
Unit tests for the Retail Trends Analyzer
"""

import unittest
import os
import json
import csv
import tempfile
from datetime import datetime
from retail_trends import RetailData, RetailTrendsAnalyzer, get_git_info


class TestRetailData(unittest.TestCase):
    """Test cases for RetailData class."""
    
    def test_retail_data_creation(self):
        """Test creating a RetailData instance."""
        data = RetailData("2024-01-15", "Laptop", "Electronics", 2, 2400.00)
        self.assertEqual(data.product, "Laptop")
        self.assertEqual(data.category, "Electronics")
        self.assertEqual(data.quantity, 2)
        self.assertEqual(data.revenue, 2400.00)
        self.assertIsInstance(data.date, datetime)
    
    def test_retail_data_repr(self):
        """Test string representation of RetailData."""
        data = RetailData("2024-01-15", "Laptop", "Electronics", 2, 2400.00)
        repr_str = repr(data)
        self.assertIn("2024-01-15", repr_str)
        self.assertIn("Laptop", repr_str)


class TestRetailTrendsAnalyzer(unittest.TestCase):
    """Test cases for RetailTrendsAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = RetailTrendsAnalyzer()
        
        # Create a temporary CSV file for testing
        csv_fd, self.test_csv_file = tempfile.mkstemp(suffix='.csv')
        with os.fdopen(csv_fd, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'product', 'category', 'quantity', 'revenue'])
            writer.writerow(['2024-01-15', 'Laptop', 'Electronics', '2', '2400.00'])
            writer.writerow(['2024-01-16', 'T-Shirt', 'Clothing', '5', '125.00'])
            writer.writerow(['2024-01-17', 'Coffee Maker', 'Appliances', '1', '89.99'])
            writer.writerow(['2024-02-15', 'Monitor', 'Electronics', '3', '900.00'])
            writer.writerow(['2024-02-16', 'Jacket', 'Clothing', '2', '200.00'])
        
        # Create a temporary JSON file for testing
        json_fd, self.test_json_file = tempfile.mkstemp(suffix='.json')
        test_json_data = [
            {"date": "2024-01-15", "product": "Laptop", "category": "Electronics", "quantity": 2, "revenue": 2400.00},
            {"date": "2024-01-16", "product": "T-Shirt", "category": "Clothing", "quantity": 5, "revenue": 125.00},
            {"date": "2024-01-17", "product": "Coffee Maker", "category": "Appliances", "quantity": 1, "revenue": 89.99}
        ]
        with os.fdopen(json_fd, 'w') as f:
            json.dump(test_json_data, f)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)
    
    def test_load_from_csv(self):
        """Test loading data from CSV file."""
        self.analyzer.load_from_csv(self.test_csv_file)
        self.assertEqual(len(self.analyzer.data), 5)
        self.assertEqual(self.analyzer.data[0].product, "Laptop")
    
    def test_load_from_json(self):
        """Test loading data from JSON file."""
        self.analyzer.load_from_json(self.test_json_file)
        self.assertEqual(len(self.analyzer.data), 3)
        self.assertEqual(self.analyzer.data[0].product, "Laptop")
    
    def test_analyze_by_category(self):
        """Test category analysis."""
        self.analyzer.load_from_csv(self.test_csv_file)
        category_stats = self.analyzer.analyze_by_category()
        
        self.assertIn("Electronics", category_stats)
        self.assertIn("Clothing", category_stats)
        self.assertIn("Appliances", category_stats)
        
        # Check Electronics stats
        electronics = category_stats["Electronics"]
        self.assertEqual(electronics['total_revenue'], 3300.00)
        self.assertEqual(electronics['total_quantity'], 5)
    
    def test_analyze_by_product(self):
        """Test product analysis."""
        self.analyzer.load_from_csv(self.test_csv_file)
        product_stats = self.analyzer.analyze_by_product()
        
        self.assertIn("Laptop", product_stats)
        self.assertEqual(product_stats["Laptop"]['total_revenue'], 2400.00)
        self.assertEqual(product_stats["Laptop"]['total_quantity'], 2)
    
    def test_identify_top_products(self):
        """Test identifying top products."""
        self.analyzer.load_from_csv(self.test_csv_file)
        top_products = self.analyzer.identify_top_products(3)
        
        self.assertEqual(len(top_products), 3)
        # Laptop should be first with highest revenue
        self.assertEqual(top_products[0][0], "Laptop")
        self.assertEqual(top_products[0][1], 2400.00)
    
    def test_identify_trending_categories(self):
        """Test identifying trending categories."""
        self.analyzer.load_from_csv(self.test_csv_file)
        trending = self.analyzer.identify_trending_categories()
        
        self.assertGreater(len(trending), 0)
        # Electronics should be first
        self.assertEqual(trending[0][0], "Electronics")
    
    def test_calculate_growth_rate(self):
        """Test growth rate calculation."""
        self.analyzer.load_from_csv(self.test_csv_file)
        growth_data = self.analyzer.calculate_growth_rate()
        
        self.assertIn('first_half_revenue', growth_data)
        self.assertIn('second_half_revenue', growth_data)
        self.assertIn('growth_rate_percent', growth_data)
    
    def test_generate_summary_report(self):
        """Test summary report generation."""
        self.analyzer.load_from_csv(self.test_csv_file)
        report = self.analyzer.generate_summary_report()
        
        self.assertIsInstance(report, str)
        self.assertIn("RETAIL TRENDS ANALYSIS REPORT", report)
        self.assertIn("Total Records:", report)
        self.assertIn("Total Revenue:", report)
        self.assertIn("TOP 5 PRODUCTS BY REVENUE", report)
    
    def test_empty_data_report(self):
        """Test report generation with no data."""
        report = self.analyzer.generate_summary_report()
        self.assertEqual(report, "No data available for analysis.")


class TestGitInfo(unittest.TestCase):
    """Test cases for git info functionality."""
    
    def test_get_git_info(self):
        """Test git info retrieval."""
        git_info = get_git_info()
        self.assertIsInstance(git_info, str)
        # Should contain either git info or error message
        self.assertTrue(
            "GIT REPOSITORY INFORMATION" in git_info or 
            "Error:" in git_info
        )


if __name__ == '__main__':
    unittest.main()
